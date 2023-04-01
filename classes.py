from abc import ABC, abstractmethod
import json
import requests
import os
from connector import Connector


class Engine(ABC):
    @abstractmethod
    def get_request(self):
        pass

    @staticmethod
    def get_connector(file_name):
        """ Возвращает экземпляр класса Connector """
        connect = Connector(file_name)
        return connect
        # hh_connect = Connector('hh.json')
        # sj_connect = Connector('sj.json')


class HH(Engine):
    def __init__(self):
        self.name = None

    def get_request(self, name=''):
        """Получает json с вакансиями по api"""
        self.name = name
        url = 'https://api.hh.ru/vacancies'
        params = {'text': self.name, "experience": "noExperience", 'area': 113, 'page': 0, 'per_page': 100}
        # response = requests.get(url, params=params)
        # response.close()
        list_hh = []
        for page in range(1):
            params['page'] = page
            response1 = requests.get(url, params=params)
            data1 = response1.content.decode()
            response = json.loads(data1)
            res1 = response['items']
            for i in res1:
                list_hh.append(i)

        return list_hh


class Superjob(Engine):
    def __init__(self):
        self.api_key_sj = None
        self.name = None

    def get_request(self, name=''): 
        """Получает json с вакансиями по api"""
        self.name = name
        self.api_key_sj: str = os.getenv('SUPER_JOB')
        url2 = 'https://api.superjob.ru/2.0/vacancies/'
        params2 = {'keyword': self.name, "experience": 1, "count": 100, 'page': 0}
        headers2 = {'X-Api-App-Id': 'v3.r.137434972.ee8a700b3805844e09b585e96390378700ad3dd3.996bd4d06d883979e271162feb034b2ed0b00da2'}
        list_sj = []
        for x in range(1):
            params2['page'] = x
            response1 = requests.get(url2, headers=headers2, params=params2)
            data1 = response1.content.decode()
            response12 = json.loads(data1)
            res1 = response12['objects']
            for i in res1:
                list_sj.append(i)
        return list_sj
