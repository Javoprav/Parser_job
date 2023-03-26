import json
from html2text import html2text


class Vacancy:
    """Ограничение по атрибутам в пользу скорости"""
    __slots__ = ('name', 'url', 'description', 'salary', 'company_name', 'range_vac_hh')

    def __init__(self, *args, **kwargs):
        pass

    def __str__(self):
        pass


class CountMixin:

    @staticmethod
    def get_count_of_vacancy(file):
        """Вернуть количество вакансий от текущего сервиса."""
        with open(file, encoding='utf-8') as f:
            data = json.load(f)
            f.close()
            return len(data)


class HHVacancy(Vacancy, CountMixin):  # add counter mixin
    """ HeadHunter Vacancy """
    range_vac_hh = []

    def __init__(self, dict_vac, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = dict_vac['name']
        self.url = dict_vac['alternate_url']
        # url_description = dict['url']
        # response = requests.get(url_description)
        # response_decode = response.content.decode()
        # response_py = json.loads(response_decode)
        # vacancies_html = response_py['description']
        # vacancies_txt = html2text(vacancies_html)
        snippet_html = dict_vac['snippet']['requirement']
        responsibility_html = dict_vac['snippet']['responsibility']
        snippet = f'{snippet_html}\n{responsibility_html}'
        description = html2text(snippet).rstrip()
        # responsibility = html2text(responsibility_html)
        # self.description = vacancies_txt
        self.description = description
        if dict_vac['salary'] is None or dict_vac['salary']['from'] is None:
            self.salary = 'Не известно'
        else:
            self.salary = dict_vac['salary']['from']
        self.company_name = dict_vac['employer']['name']

    @classmethod
    def sorting(cls, vacancies):
        """Сортирует любой список вакансий по ежемесячной оплате"""
        for i in range(len(vacancies)):
            if vacancies[i]['salary'] is not None and vacancies[i]['salary']['from'] is not None:
                cls.range_vac_hh.append(vacancies[i])
        cls.range_vac_hh.sort(key=lambda x: x['salary']['from'], reverse=True)
        return cls.range_vac_hh

    @classmethod
    def get_top(cls):
        """Возвращает {top_count} записей из вакансий по зарплате"""
        all_vac_sort_hh = []
        for i in range(10):
            vacancy = HHVacancy(cls.range_vac_hh[i])
            all_vac_sort_hh.append(vacancy)
        return all_vac_sort_hh

    def __str__(self):
        return f'HH.ru: Название вакансии: {self.name}, \n' \
               f'Ссылка: {self.url}, Компания: \n{self.company_name} \n' \
               f'Описание: {self.description}\n' \
               f'зарплата: {self.salary} руб/мес\n'

    def __repr__(self):
        return f'HH.ru: Название вакансии: {self.name}, \n' \
               f'Ссылка: {self.url}, Компания: \n{self.company_name} \n' \
               f'Описание: {self.description}\n' \
               f'зарплата: {self.salary} руб/мес\n'


class SJVacancy(Vacancy, CountMixin):  # add counter mixin
    """ SuperJob Vacancy """
    range_vac_sj = []

    def __init__(self, dict_vac, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = dict_vac['profession']
        self.url = dict_vac['link']
        vacancyRichText = dict_vac['vacancyRichText']
        candidate = dict_vac['candidat']
        url_description = f'{candidate}\n{vacancyRichText}'
        vacancies_txt = html2text(url_description)
        self.description = vacancies_txt
        self.salary = dict_vac['payment_from']
        self.company_name = dict_vac['firm_name']

    @classmethod
    def sorting(cls, vacancies):
        """Сортирует любой список вакансий по ежемесячной оплате"""
        for i in range(len(vacancies)):
            if vacancies[i]['payment_from'] is not None and vacancies[i]['payment_from'] != 0:
                cls.range_vac_sj.append(vacancies[i])
        cls.range_vac_sj.sort(key=lambda x: x['payment_from'], reverse=True)
        return cls.range_vac_sj

    @classmethod
    def get_top(cls):
        """Возвращает {top_count} записей из вакансий по зарплате"""
        all_vac_sort_sj = []
        for i in range(10):
            vacancy = SJVacancy(cls.range_vac_sj[i])
            all_vac_sort_sj.append(vacancy)
        return all_vac_sort_sj

    def __str__(self):
        return f'superjob.ru: Название вакансии: {self.name}, \n' \
               f'url: {self.url}, Компания: \n{self.company_name} \n' \
               f'Описание: {self.description}'\
               f'зарплата: {self.salary} руб/мес\n'

    def __repr__(self):
        return f'superjob.ru: Название вакансии: {self.name}, \n' \
               f'url: {self.url}, Компания: \n{self.company_name} \n' \
               f'Описание: {self.description}'\
               f'зарплата: {self.salary} руб/мес\n'
