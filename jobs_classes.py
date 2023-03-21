import json, requests
from html2text import html2text

class Vacancy:
    __slots__ = ('name', 'url', 'description', 'salary', 'company_name')

    def __init__(self, *args, **kwargs):
        pass

    def __str__(self):
        pass


class CountMixin:

    def get_count_of_vacancy(self, file):
        """
        Вернуть количество вакансий от текущего сервиса.
        Получать количество необходимо динамически из файла.
        """
        with open(file, encoding='utf-8') as f:
            data = json.load(f)
            f.close()
            return len(data)


class HHVacancy(Vacancy, CountMixin):  # add counter mixin
    """ HeadHunter Vacancy """
    def __init__(self, dict, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = dict['name']
        self.url = dict['alternate_url']
        url_description = dict['url']
        response = requests.get(url_description)
        response_decode = response.content.decode()
        response_py = json.loads(response_decode)
        vacancies_html = response_py['description']
        vacancies_txt = html2text(vacancies_html)
        self.description = vacancies_txt
        if dict['salary'] is None or dict['salary']['from'] is None:
            self.salary = 'Не известно'
        else:
            self.salary = dict['salary']['from']
        self.company_name = dict['employer']['name']

    def __str__(self):
        return f'HH.ru: Название вакансии: {self.name}, \n' \
               f'url: {self.url}, Компания: \n{self.company_name}\n' \
               f'Описание: {self.description},\n ' \
               f'зарплата: {self.salary} руб/мес'

    def __repr__(self):
        return f'HH.ru: Название вакансии: {self.name}, \n' \
               f'url: {self.url}, Компания: \n{self.company_name}\n' \
               f'Описание: {self.description},\n ' \
               f'зарплата: {self.salary} руб/мес'


class SJVacancy(Vacancy, CountMixin):  # add counter mixin
    """ SuperJob Vacancy """
    def __init__(self, dict, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = dict['profession']
        self.url = dict['link']
        vacancyRichText = dict['vacancyRichText']
        candidat = dict['candidat']
        url_description = f'{candidat}\n{vacancyRichText}'
        vacancies_txt = html2text(url_description)
        self.description = vacancies_txt
        self.salary = dict['payment_from']
        self.company_name = dict['firm_name']

    def __str__(self):
        return f'superjob.ru: Название вакансии: {self.name}, \n' \
               f'url: {self.url}, Компания: \n{self.company_name}\n' \
               f'Описание: {self.description},\n ' \
               f'зарплата: {self.salary} руб/мес'

    def __repr__(self):
        return f'superjob.ru: Название вакансии: {self.name}, \n' \
               f'url: {self.url}, Компания: \n{self.company_name}\n' \
               f'Описание: {self.description},\n ' \
               f'зарплата: {self.salary} руб/мес'


def sorting(vacancies):
    """ Должен сортировать любой список вакансий по ежемесячной оплате (gt, lt magic methods) """
    pass


def get_top(vacancies, top_count):
    """ Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """
    pass