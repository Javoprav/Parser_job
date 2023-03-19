from abc import ABC, abstractmethod
from pprint import pprint
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
        """Получает json с вакансиями по api"""
        self.name = name
        url = 'https://api.hh.ru/vacancies'
        params = {'text': self.name, 'area': 113, 'page': 0}
        response = requests.get(url, params=params)
        list_hh = []
        if response.ok:
            data = response.json()
            pages = data['pages']
            for page in range(pages):
                params['page'] = page
                if response.ok:
                    data = response.json()
                    vacancies = data['items']
                    # return vacancies
                    for vacancy in vacancies:
                        list_hh.append(vacancy)
            return list_hh
        else:
            pprint('Error:', response.status_code)
        # vacancies = response.json()
        # for vacancy in vacancies['items']:
        #     pprint(vacancy)
        # return vacancies


class Superjob(Engine):
    def __init__(self):
        self.name = None

    def get_request(self, name):
        """Получает json с вакансиями по api"""
        self.name = name
        url2 = 'https://api.superjob.ru/2.0/vacancies/'
        params2 = {'town': '4', 'keyword': self.name, "count": 10000, 'geo[c][0]': '1', 'geo[c][1]': '4'}
        headers2 = {'X-Api-App-Id': 'v3.r.137434972.ee8a700b3805844e09b585e96390378700ad3dd3.996bd4d06d883979e271162feb034b2ed0b00da2'}
        response2 = requests.get(url2, headers=headers2, params=params2)
        vacancies2 = response2.json()
        return vacancies2