from monostate import MonostateMeta
from dataclasses import dataclass


@dataclass
class MonostateDB(MonostateMeta):
    connection: bool

    def get_connection(self):
        if self.connection is True:
            print(f"Успешное подключение")
        else:
            print(f"Ошибка подключения")
        print(f"ID-DB: {id(self)}")
