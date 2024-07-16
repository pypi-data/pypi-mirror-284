import socket
import re
import json
import http.client
from datetime import datetime, time
from peasys.pea_exception import *
from peasys.pea_response import *

class PeaClient:
    '''
    Represents the client part of the client-server architecture of the Peasys technology.
    '''
    def __init__(self, dns_server_name, partition_name, port, username, password, id_client, online_version=True, retrieve_statistics=False) -> None:
        '''Initialize a new instance of PeaClient the class.
        
        Args
        ------
        dns_server_name (str):
            DNS name of the remote AS/400 server.
        partition_name (str) :
            Name of the partition.
        port (int):
            Port used for the data exchange between the client and the server.
        username (str):
            Username of the AS/400 profile used for connexion.
        password (str):
            Password of the AS/400 profile used for connexion.
        id_client (str):
            ID of the client account on the DIPS website.
        online_version (boolean):
            Set to true if you want to use the online version of Peasys. Visit https://dips400.com/docs/connexion" for more informations.
        retrieve_statistics (boolean):
            If set to true, statistics of Peasys' use will be sent to a database. Default is False.

        Raises
        ------
        PeaInvalidCredentialsException
            If username || password are wrong.
        PeaInvalidLicenseKeyException
            If your subscription is not valid.
        ConnectionError
            If client couldn't connect to remote server.
        '''
        
        if(not dns_server_name or not port or not username or not password or not id_client):
            raise PeaInvalidCredentialsException("Fields of the PeaClient instance cannot be empty.")
        
        self._dns_server_name = dns_server_name
        self._port = port
        self._partition_name = partition_name
        self._username = username
        self._password = password
        self._id_client = id_client
        self._retreive_statitics = retrieve_statistics
        
        # retrieve connexion token online
        token = "xqdsg27010wmca6052009050000000IDSP1tiupozxreybjhlk" # default token in case of offline verification
        if online_version:
            try:
                host = "dips400.com"
                self.__conn = http.client.HTTPSConnection(host)
                self.__conn.request("GET", f"/api/license-key/retrieve-token/{partition_name}/{id_client}")
                data = self.__conn.getresponse().read()
                decoded_data = json.loads(data)
                token = decoded_data["token"]
                
                if not decoded_data["isValid"]:
                    raise PeaInvalidLicenseKeyException("Your subscription is not valid, visit https://dips400.com/account/subscriptions for more information.")
                
            except PeaInvalidLicenseKeyException as error:
                raise error
            except:
                pass # If dips400.com doesn't respond, let's try an affline verification with the offline token
        

        self._clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self._clientsocket.connect((dns_server_name, port))
        except:
            raise ConnectionError("Error connecting the socket to the client")

        login = username.ljust(10, " ") + token.ljust(50, " ") + password
        self._clientsocket.sendall(login.encode('iso-8859-1'))

        self._connexion_status = self._clientsocket.recv(1).decode('iso-8859-1')

        self._connexion_message = ""
        match self._connexion_status:
            case "1":
                if online_version:
                    self.__send_statitics({"Name": "username", "IdClient": id_client, "PartitionName" : dns_server_name})
                self._connexion_message = "Connected"
                self._connexion_status = 1
            case "2":
                self._connexion_message = "Unable to set profile, check profile validity."
                self._connexion_status = 2
                raise PeaInvalidCredentialsException("Unable to set profile, check profile validity.")
            case "3":
                self._connexion_message = "Invalid credential"
                self._connexion_status = 3
                raise PeaInvalidCredentialsException("Invalid username or password, check again.")
            case "B":
                self._connexion_message = "Peasys Online : your token connexion is no longer valid, retry to connect."
                self._connexion_status = 5
                raise PeaInvalidCredentialsException("Peasys Online : your token connexion is no longer valid, retry to connect.")
            case "D":
                self._connexion_message = "Peasys Online : the partition name you provided doesn't match the actual name of the machine."
                self._connexion_status = 6
                raise PeaConnexionException("Peasys Online : the partition name you provided doesn't match the actual name of the machine.")
            case "E":
                self._connexion_message = "You reached the max number of simultaneously connected peasys users for that partition and license key. Contact us for upgrading your license."
                self._connexion_status = 7
                raise PeaConnexionException("You reached the max number of simultaneously connected peasys users for that partition and license key. Contact us for upgrading your license.")
            case "F":
                self._connexion_message = "Your license is no longer valid. Subscribe to another license in order to continue using Peasys."
                self._connexion_status = 8
                raise PeaConnexionException("Your license is no longer valid. Subscribe to another license in order to continue using Peasys.")
            case "0" | "A" | "C" | "G":
                self._connexion_message = "Error linked to DIPS source code. Please, contact us immediatly to fix the issue."
                self._connexion_status = -1
                raise PeaConnexionException("Error linked to DIPS source code. Please, contact us immediatly to fix the issue.")
            case _:
                raise PeaConnexionException("Exception during connexion process, contact us for more informations")    
        
    def execute_select(self, query) -> PeaSelectResponse:
        '''Sends the SELECT SQL query to the server that execute it and retreive the desired data.
        
        Args
        ------
        query (str):
            SQL query that should starts with the SELECT keyword

        Raises
        ------
        PeaInvalidSyntaxQueryException
            If the query syntax is invalid.
        '''
        if(not query): 
            raise PeaInvalidSyntaxQueryException("Query should not be either null or empty")
        if(not query.upper().startswith("SELECT")):
            raise PeaInvalidSyntaxQueryException("Query should starts with the SELECT SQL keyword")
        
        (result, columns_name, row_count, sql_state, sql_message) = self.__build_data(query)
    
        return PeaSelectResponse(sql_state == "00000", sql_message, sql_state, result, row_count, columns_name)
    
    def execute_update(self, query) -> PeaUpdateResponse:
        '''Sends the UPDATE SQL query to the server that execute it and retreive the desired data.
        
        Args
        ------
        query (str):
            SQL query that should starts with the SELECT keyword

        Raises
        ------
        PeaInvalidSyntaxQueryException
            If the query syntax is invalid.
        '''
        if(not query): 
            raise PeaInvalidSyntaxQueryException("Query should not be either null or empty")
        if(not query.upper().startswith("UPDATE")):
            raise PeaInvalidSyntaxQueryException("Query should starts with the UPDATE SQL keyword")
        
        (row_count, sql_state, sql_message) = self.__modify_table(query)
        has_succeeded = sql_state == "00000" or sql_state == "01504"
        return PeaUpdateResponse(has_succeeded, sql_state, sql_message, row_count)

    def execute_create(self, query) -> PeaCreateResponse:
        '''Sends the CREATE SQL query to the server that execute it and retreive the desired data.
        
        Args
        ------
        query (str):
            SQL query that should starts with the SELECT keyword

        Raises
        ------
        PeaInvalidSyntaxQueryException
            If the query syntax is invalid.
        '''
        if(not query): 
            raise PeaInvalidSyntaxQueryException("Query should not be either null or empty")
        if(not query.upper().startswith("CREATE")):
            raise PeaInvalidSyntaxQueryException("Query should starts with the CREATE SQL keyword")
        
        (_, sql_state, sql_message) = self.__modify_table(query)

        query_words = query.split(' ')

        # retreive table schema if a table has been created 
        tb_schema = None
        if (query_words[1].ToUpper() == "TABLE"):
            names = query_words[2].split('/')
            tb_query = """SELECT COLUMN_NAME, ORDINAL_POSITION, DATA_TYPE, LENGTH, NUMERIC_SCALE, IS_NULLABLE, IS_UPDATABLE, NUMERIC_PRECISION
                    FROM QSYS2.SYSCOLUMNS WHERE SYSTEM_TABLE_NAME = '""" + names[1].upper() + "' AND SYSTEM_TABLE_SCHEMA = '" + names[0].upper() + "'"
            (result, _, row_count, _, _) = self.__build_data(tb_query)
            for i in range(0, row_count):
                tb_schema[result["column_name"][i]] = ColumnInfo(result["column_name"][i], result["ordinal_position"][i], result["data_type"][i], result["length"][i], 
                    result["numeric_scale"][i], result["is_nullable"][i], result["is_updatable"][i], result["numeric_precision"][i])

        match query_words[1].upper():
            case "TABLE":
                return PeaCreateResponse(sql_state == "00000", sql_message, sql_state, "", "", tb_schema)
            case "INDEX":
                return PeaCreateResponse(sql_state == "00000", sql_message, sql_state, "", query_words[2], tb_schema)
            case "DATABASE":
                return PeaCreateResponse(sql_state == "00000", sql_message, sql_state, query_words[2], "", tb_schema),
            case _ :
                raise PeaInvalidSyntaxQueryException("Syntax invalid in query : " + query)

    def execute_delete(self, query) -> PeaDeleteResponse:
        '''Sends the DELETE SQL query to the server that execute it and retreive the desired data.
        
        Args
        ------
        query (str):
            SQL query that should starts with the SELECT keyword

        Raises
        ------
        PeaInvalidSyntaxQueryException
            If the query syntax is invalid.
        '''
        if(not query): 
            raise PeaInvalidSyntaxQueryException("Query should not be either null or empty")
        if(not query.upper().startswith("DELETE")):
            raise PeaInvalidSyntaxQueryException("Query should starts with the DELETE SQL keyword")
        
        (row_count, sql_state, sql_message) = self.__modify_table(query)

        return PeaDeleteResponse(sql_state == "00000", sql_message, sql_state, row_count)

    def execute_alter(self, query, retreive_table_schema: False) -> PeaAlterResponse:
        '''Sends the ALTER SQL query to the server that execute it and retreive the desired data.
        
        Args
        ------
        query (str):
            SQL query that should starts with the SELECT keyword

        Raises
        ------
        PeaInvalidSyntaxQueryException
            If the query syntax is invalid.
        '''
        if(not query): 
            raise PeaInvalidSyntaxQueryException("Query should not be either null or empty")
        if(not query.upper().startswith("ALTER")):
            raise PeaInvalidSyntaxQueryException("Query should starts with the ALTER SQL keyword")

        (_, sql_state, sql_message) = self.__modify_table(query)

        # reteive table schema if wanted
        tb_schema = dict()
        if (retreive_table_schema):
            query_words = query.split(' ')
            names = query_words[2].split('/')
            tb_query = """SELECT COLUMN_NAME, ORDINAL_POSITION, DATA_TYPE, LENGTH, NUMERIC_SCALE, IS_NULLABLE, IS_UPDATABLE, NUMERIC_PRECISION
                    FROM QSYS2.SYSCOLUMNS WHERE SYSTEM_TABLE_NAME = '""" + names[1].upper() + "' AND SYSTEM_TABLE_SCHEMA = '" + names[0].upper() + "'"
                    
            (result, _, row_count, _, _) = self.__build_data(tb_query)
            
            for i in range(0, row_count):
                tb_schema[result["column_name"][i]] = ColumnInfo(result["column_name"][i], result["ordinal_position"][i], result["data_type"][i], result["length"][i], 
                    result["numeric_scale"][i], result["is_nullable"][i], result["is_updatable"][i], result["numeric_precision"][i])
        
        return PeaAlterResponse(sql_state == "00000", sql_message, sql_state, tb_schema)

    def execute_drop(self, query) -> PeaDropResponse:
        '''Sends the DROP SQL query to the server that execute it and retreive the desired data.
        
        Args
        ------
        query (str):
            SQL query that should starts with the SELECT keyword

        Raises
        ------
        PeaInvalidSyntaxQueryException
            If the query syntax is invalid.
        '''
        if(not query): 
            raise PeaInvalidSyntaxQueryException("Query should not be either null or empty")
        if(not query.upper().startswith("DROP")):
            raise PeaInvalidSyntaxQueryException("Query should starts with the DROP SQL keyword")

        (_, sql_state, sql_message) = self.__modify_table(query)

        return PeaDropResponse(sql_state == "00000", sql_message, sql_state)

    def execute_insert(self, query) -> PeaInsertResponse:
        '''Sends the INSERT SQL query to the server that execute it and retreive the desired data.
        
        Args
        ------
        query (str):
            SQL query that should starts with the SELECT keyword

        Raises
        ------
        PeaInvalidSyntaxQueryException
            If the query syntax is invalid.
        '''
        if(not query): 
            raise PeaInvalidSyntaxQueryException("Query should not be either null or empty")
        if(not query.upper().startswith("INSERT")):
            raise PeaInvalidSyntaxQueryException("Query should starts with the INSERT SQL keyword")

        (row_count, sql_state, sql_message) = self.__modify_table(query)

        return PeaInsertResponse(sql_state == "00000", sql_state, sql_message, row_count)
    
    def execute(self, query) -> PeaResponse:
        '''Sends the SQL query to the server that execute it and retreive the desired data. Used to send more complex SQL queries to the server.
        
        Args
        ------
        query (str):
            SQL query.
        '''

        (row_count, sql_state, sql_message) = self.__modify_table(query)

        return PeaResponse(sql_state == "00000", sql_state, sql_message, row_count)
    
    def execute_command(self, command) -> PeaCommandResponse:
        '''Sends a OS/400 command to the server and retreives the potential warning messages.
        
        Args
        ------
        command (str):
            OS/400 command to be executed by the server.

        Raises
        ------
        PeaInvalidSyntaxQueryException
            If the query syntax is invalid.
        '''
        customCmd = "exas" + command + "dipsjbiemg"
        descriptionOffset = 112
        rgx = "[^a-zA-Z0-9 áàâäãåçéèêëíìîïñóòôöõúùûüýÿæœÁÀÂÄÃÅÇÉÈÊËÍÌÎÏÑÓÒÔÖÕÚÙÛÜÝŸÆŒ._'*/:-]"
        rx = "C[A-Z]{2}[0-9]{4}"
        
        result_raw = self.__retreive_data(customCmd)
        result = []
        try:
            
            for match in re.finditer(rx, result_raw):
                if (not match.group().startswith("CPI") and match.span()[0] + descriptionOffset < len(result_raw)):
                    description = result_raw[match.span()[0] + descriptionOffset:]
                    description = description[:description.index('.')]
                    description = re.sub(rgx, "", description)
                    
                    result.append(match.group() + " " + description)

            return PeaCommandResponse(result)
        except:
            return PeaCommandResponse(result)

    def disconnect(self):
        '''Closes the TCP connexion with the server.
        '''
        self._clientsocket.sendall("stopdipsjbiemg".encode())
        self._clientsocket.flu
        self._clientsocket.close()

    def __modify_table(self, query):
        _end_pack = "dipsjbiemg"

        command = "updt" + query + _end_pack
        header = self.__retreive_data(command)
        
        sql_state = header[:5]
        sql_message = header[5:].strip()
        
        # send statitics if wanted
        if self._retreive_statitics:
            self.__send_statitics({"Name": "data_in", "Bytes": len(query.encode('utf-8')), "IdClient": self._id_client, "PartitionName" : self._dns_server_name})
            self.__send_statitics({"Name": "data_out", "Bytes": len(header.encode('utf-8')), "IdClient": self._id_client, "PartitionName" : self._dns_server_name})
            self.__send_statitics({"Name": "log", "UserName" : self.username, "Query": query.split(' ')[0], "SqlCode":sql_state, "SqlMessage": sql_message, "IdClient": self._id_client, "PartitionName" : self._dns_server_name})

        row_count = 0
        if (query.upper().startswith("INSERT") or query.upper().startswith("UPDATE") or query.upper().startswith("DELETE")):
            row_count = int(sql_message[:1]) if sql_state == "00000" else 0

        return (row_count, sql_state, sql_message)

    def __build_data(self, query):
        _end_pack = "dipsjbiemg"
        
        header_cmd = "geth" + query + _end_pack
        header = self.__retreive_data(header_cmd)

        sql_state = "00000"
        sql_message = "SELECT query executed well"
        try:
            json_header = json.loads(header)
        except:
            sql_state = header[1:5]
            sql_message = header[6:]
            return (None, None, 0, sql_state, sql_message)
            
        nb_col = len(json_header)

        data_command = "getd" + query + _end_pack
        data = self.__retreive_data(data_command)
        
        # send statitics if wanted
        if self._retreive_statitics:
            self.__send_statitics({"Name": "data_in", "Bytes": len(query.encode('utf-8')), "IdClient": self._id_client, "PartitionName" : self._dns_server_name})
            self.__send_statitics({"Name": "data_out", "Bytes": len(data.encode('utf-8')), "IdClient": self._id_client, "PartitionName" : self._dns_server_name})
            self.__send_statitics({"Name": "log", "UserName" : 
                self.username, "Query": query.split(' ')[0], "SqlCode":sql_state, "SqlMessage": sql_message, "IdClient": self._id_client, "PartitionName" : self._dns_server_name})

        sum_precision = 0
        result = dict()
        columns_name = []
        for row in json_header:
            sum_precision += int(row["prec"])
            colname = row["name"].strip().lower()
            result[colname] = []
            columns_name.append(colname)

        nb_row = int(len(data) / sum_precision)
       
        pointer = 0
        while (not (pointer == len(data))): 
            for m in range(0, nb_col):
                type = int(json_header[m]["type"])
                scale = int(json_header[m]["scal"])
                precision = int(json_header[m]["prec"])
                name = json_header[m]["name"].strip().lower()
                # numeric packed
                if ((type == 484 and scale != 0) or (type == 485 and scale != 0) or (type == 488 and scale != 0) or (type == 489 and scale != 0)):
                    temp_float_data = float(data[pointer:pointer+precision]) / pow(10, scale)
                    pointer += precision
                    result[name].append(temp_float_data)
                # long
                elif (type == 492 or type == 493):
                    result[name].append(int(data[pointer:pointer+20]))
                    pointer += 20
                # int
                elif (type == 496 or type == 497):
                    result[name].append(int(data[pointer:pointer+10]))
                    pointer += 10
                # short
                elif (type == 500 or type == 501):
                    result[name].append(int(data[pointer:pointer+5]))
                    pointer += 5
                # string, date, time, timestamp
                else:
                    if (type == 389):
                        result[name].append(time.fromisoformat(data.Substring(pointer, precision[m])))
                    elif (type == 385):
                        result[name].append(datetime.strptime(data[pointer: pointer+precision].strip(), "%d/%m/%y"))
                    else:
                        result[name].append(data[pointer: pointer+precision].strip())
                    pointer += precision

        return (result, columns_name, nb_row, sql_state, sql_message)
    
    def __retreive_data(self, command) -> str:
        _end_pack = "dipsjbiemg"
        self._clientsocket.sendall(command.encode('iso-8859-1'))

        data = "[" if command.startswith("geth") else ""
        while (len(data) < len(_end_pack) or data[-len(_end_pack):] != _end_pack):
            data += str(self._clientsocket.recv(1).decode('iso-8859-1'))

        return data[:len(data)-len(_end_pack)]
    
    def __send_statitics(self, data) -> None:
        body = json.dumps(data, default=str)
        self.__conn.request("PATCH", f"/api/license-key/update" ,body=body, headers={"Content-Type": "application/json"})
        _ = self.__conn.getresponse().read()
    
    @property
    def dns_server_name(self) -> str:
        '''
        DNS name of the remote AS/400 server.
        '''
        return self._dns_server_name
    
    @property
    def port(self) -> int:
        '''
        Port used for the data exchange between the client and the server.
        '''
        return self._port
    
    @property
    def username(self) -> str:
        '''
        Username of the AS/400 profile used for connexion.
        '''
        return self._username
    
    @property
    def password(self) -> str:
        '''
        Password of the AS/400 profile used for connexion.
        '''
        return self._password
    
    @property
    def license_key(self) -> str:
        '''
        License key delivered by DIPS after subscription.
        '''
        return self._license_key
    
    @property
    def connexion_status(self) -> str:
        '''
        Status of the connexion with the AS/400 server.
        '''
        return self._connexion_status
    
    @property
    def connexion_message(self) -> int:
        '''
        Message of the connexion with the AS/400 server.
        '''
        return self._connexion_message
    
    @property
    def retrieve_statistics(self) -> bool:
        '''
        Boolean set to true if statitics of Peasys' use are saved
        '''
        return self._retreive_statitics