from abc import ABC, abstractmethod
import requests


class Engine(ABC):
    @abstractmethod
    def get_request(self):
        pass

    @staticmethod
    def get_connector(file_name):
        """ Возвращает экземпляр класса Connector """
        pass


class HH(Engine):
    def __init__(self):
        self.name = None

    def get_request(self, name):
        self.name = name
        url = 'https://api.hh.ru/vacancies'
        params = {'text': self.name, 'area': '1'}
        response = requests.get(url, params=params)
        vacancies = response.json()
        return vacancies


class Superjob(Engine):
    def __init__(self):
        self.name = None

    def get_request(self, name):
        self.name = name
        url2 = 'https://api.superjob.ru/2.0/vacancies/'
        params2 = {'keyword': self.name, 'geo[c][0]': '1', 'geo[c][1]': '4'}
        headers2 = {'X-Api-App-Id': 'v3.r.137434972.ee8a700b3805844e09b585e96390378700ad3dd3.996bd4d06d883979e271162feb034b2ed0b00da2'}
        response2 = requests.get(url2, headers=headers2, params=params2)
        vacancies2 = response2.json()
        return vacancies2