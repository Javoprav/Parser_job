from abc import ABC, abstractmethod
import json
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
        params = {'text': self.name, "experience": "noExperience", 'area': 113, 'page': 0, 'per_page': 100}
        response = requests.get(url, params=params)
        data = response.content.decode()
        response.close()
        list_hh = []
        dict_hh = {}
        # pages = response['pages']
        for page in range(20):
            params['page'] = page
            response1 = requests.get(url, params=params)
            data1 = response1.content.decode()
            response = json.loads(data1)
            res1 = response['items']
            # pprint(res1)
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
        params2 = {'keyword': self.name, "experience": 1, "count": 100, 'page': 0}
        headers2 = {'X-Api-App-Id': self.api_key_sj}
        list_sj = []
        for x in range(20):
            params2['page'] = x
            response1 = requests.get(url2, headers=headers2, params=params2)
            data1 = response1.content.decode()
            response12 = json.loads(data1)
            res1 = response12['objects']
            for i in res1:
                list_sj.append(i)
        return list_sj
