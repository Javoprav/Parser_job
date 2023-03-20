from abc import ABC, abstractmethod
from pprint import pprint
import requests, json, os


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
        """Получает json с вакансиями по api"""
        self.name = name
        url = 'https://api.hh.ru/vacancies'
        params = {'text': self.name, 'area': 113, 'page': 0, 'per_page': 100}
        response = requests.get(url, params=params)
        data = response.content.decode()
        response.close()
        response = json.loads(data)
        # pprint(response)
        list_hh = []
        pages = response['pages']
        for page in range(pages):
            params['page'] = page
            response1 = requests.get(url, params=params)
            data1 = response1.content.decode()
            response12 = json.loads(data1)
            res1 = response12['items']
            for i in res1:
                list_hh.append(i)
        return list_hh


class Superjob(Engine):
    def __init__(self):
        self.name = None

    def get_request(self, name):
        """Получает json с вакансиями по api"""
        self.name = name
        self.api_key_sj: str = os.getenv('SUPER_JOB')
        url2 = 'https://api.superjob.ru/2.0/vacancies/'
        params2 = {'town': '4', 'keyword': self.name, "count": 10000, 'geo[c][0]': '1', 'geo[c][1]': '4'}
        headers2 = {'X-Api-App-Id': self.api_key_sj}
        response2 = requests.get(url2, headers=headers2, params=params2)
        vacancies2 = response2.json()
        return vacancies2