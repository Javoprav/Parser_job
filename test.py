from abc import ABC, abstractmethod
from pprint import pprint
import requests, json
from jobs_classes import *

with open('hh.json', encoding='utf-8') as f:
    data = json.load(f)
    pprint(len(data))
    pprint(data[0])
    vac1 = HHVacancy(data[0])

print(vac1)
