from monostate_db import MonostateDB
from singleton_db import SingletonDB

if __name__ == "__main__":
    print()
    s_db_1 = SingletonDB(True)
    s_db_2 = SingletonDB(False)
    s_db_1.get_connection()
    s_db_2.get_connection()
    print()
    s_db_3 = MonostateDB(True)
    s_db_4 = MonostateDB(False)
    s_db_3.get_connection()
    s_db_4.get_connection()
    print()
