from singleton import SingletonMeta
from dataclasses import dataclass


@dataclass
class SingletonDB(metaclass=SingletonMeta):
    connection: bool

    def get_connection(self):
        if self.connection is True:
            print(f"Успешное подключение")
        else:
            print(f"Ошибка подключения")
        print(f"ID-DB: {id(self)}")
