from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def get_request(self):
        pass

    @staticmethod
    def get_connector(file_name):
        """ Возвращает экземпляр класса Connector """
        pass

class HH(Engine):
    def get_request(self):
        pass

class Superjob(Engine):
    def get_request(self):
        pass