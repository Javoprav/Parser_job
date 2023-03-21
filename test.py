from abc import ABC, abstractmethod
from pprint import pprint
import requests, json, os
from jobs_classes import *

with open('hh.json', encoding='utf-8') as f:
    data = json.load(f)
    pprint(len(data))
    pprint(data[0])
    # for i in data:
    #     print(i['url'])
    # pprint(data[11])
    # vac2 = SJVacancy(data[11])
    # print(vac2.get_count_of_vacancy('sj.json'))
# print(vac2)

# with open('sj.json', 'r', encoding='utf-8') as f:
#     pprint(len(*f))
#     data = f.readline()
#     pprint(data)
#     f.close()
#
# array = open('hh.json', 'r', encoding='utf-8')
# print(array[0:100])