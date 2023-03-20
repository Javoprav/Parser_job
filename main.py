import requests, json, time, os
from pprint import pprint
from classes import *

hh = HH()
sj = Superjob()
if __name__ == '__main__':
    user_input = input('Введите название вакансии: ')
    hh_json = hh.get_request(user_input)
    sj_json = sj.get_request(user_input)
    with open('hh.json', 'w', encoding='utf8') as f:
        json.dump(hh_json, f,  ensure_ascii=False)
        f.close()

    with open('sj.json', 'w', encoding='utf8') as f:
        json.dump(sj_json, f, ensure_ascii=False)
        f.close()
