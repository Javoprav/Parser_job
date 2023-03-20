from abc import ABC, abstractmethod
from pprint import pprint
import requests, json, os
from jobs_classes import *

with open('sj.json', encoding='utf-8') as f:
    data = json.load(f)
    pprint(len(data))
    pprint(data[11])
    vac2 = SJVacancy(data[1])
print(vac2)
