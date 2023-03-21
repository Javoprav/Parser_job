from abc import ABC, abstractmethod
from pprint import pprint
import requests, json, os
from jobs_classes import *

# with open('sj.json', encoding='utf-8') as f:
#     data = json.load(f)
#     pprint(len(data))
    # for i in data:
    #     print(i['address'])
    # pprint(data[11])
    # vac2 = SJVacancy(data[11])
    # print(vac2.get_count_of_vacancy('sj.json'))
# print(vac2)

with open('hh.json', encoding='utf-8') as f:
    data = json.load(f)
    pprint(len(data))
    # for i in data:
    #     print(i['address'])
    # pprint(data[11])
    vac1 = HHVacancy(data[0])
    print(vac1)
    # vac2 = SJVacancy(data[11])
    # print(vac2.get_count_of_vacancy('sj.json'))
    f.close()
# print(vac2)