import requests, json, time, os
from pprint import pprint
from classes import *

hh = HH()
sj = Superjob()
if __name__ == '__main__':
    user_input = input('Введите название вакнсии: ')
    pprint(hh.get_request(user_input))
    pprint(sj.get_request(user_input))