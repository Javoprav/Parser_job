from abc import ABC, abstractmethod
from pprint import pprint
import requests, json, os
from jobs_classes import *
from connector import *

with open('hh.json', encoding='utf-8') as f:
    data = json.load(f)
    pprint(len(data))


#     # pprint(data)
#     myDict = {i: data[i] for i in range(0, len(data), 1)} # чудный словарик получился