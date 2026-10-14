class DBConnection:
    _instance = None
    dbconnection = None

    def __new__ (cls, connection_string : str):
        if not cls._instance:
            cls._instance = super(DBConnection,cls).__new__(cls)
            cls.dbconnection = connection_string
        return cls._instance

db = DBConnection("sqlserver:mcasatti@localhost/DBMAIN")
print (db.dbconnection)

db2 = DBConnection("oracle:martincito@servidor/DATABASE")
print (db.dbconnection)

