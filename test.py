from abc import ABC, abstractmethod
from pprint import pprint
import requests, json, os
from jobs_classes import *
from connector import *


# with open('hh.json', encoding='utf-8') as f:
#     data = json.load(f)
#     pprint(len(data))
# def filter_data(query):
#     with open('hh.json', 'r') as f:
#         data = json.load(f)
#         filtered_data = [row for row in data if all(row.get(key) == value for key, value in query.items())]
#     return filtered_data
#
# pprint(filter_data)
#
#
# data = filter_data({"area"["name"]: "Санкт-Петербург"})
# for row in data:
#     print(row['name'], row['price'])

#     # pprint(data)
#     myDict = {i: data[i] for i in range(0, len(data), 1)} # чудный словарик получился


url = 'https://api.hh.ru/vacancies'
params = {'text': "Python разработчик", "description": 'required', "experience": "noExperience", 'area': 113, 'page': 0, 'per_page': 100}
response = requests.get(url, params=params)
data1 = response.content.decode()
response1 = json.loads(data1)
pprint(response1)

