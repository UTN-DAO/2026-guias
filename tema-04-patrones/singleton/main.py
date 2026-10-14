"""
Demostración del patrón Singleton: la conexión es la misma aunque se pida dos
veces con cadenas distintas.
"""
from singleton import DBConnection


def main():
    db = DBConnection("sqlserver:mcasatti@localhost/DBMAIN")
    print(db.dbconnection)

    db2 = DBConnection("oracle:martincito@servidor/DATABASE")
    print(db.dbconnection)
    print("¿Es la misma instancia?", db is db2)


if __name__ == "__main__":
    main()
