import requests, json, time, os
from pprint import pprint
from classes import *
from connector import *
from jobs_classes import *

hh = HH()
sj = Superjob()
if __name__ == '__main__':
    user_input = input('Введите название вакансии: ')
    hh_json = hh.get_request(user_input)
    sj_json = sj.get_request(user_input)
    hh_connect = Connector('hh.json')
    sj_connect = Connector('sj.json')
    hh_connect.insert(hh_json)
    sj_connect.insert(sj_json)
    all_vac_hh = []
    for i in range(len(hh_json)):
        vacancy = HHVacancy(hh_json[i])
        pprint(vacancy)
        all_vac_hh.append(vacancy)
    vac_test_hh = HHVacancy(hh_json[0])
    len_vac_hh = vac_test_hh.get_count_of_vacancy('hh.json')
    print(f'Собрано вакансий с сайта hh.ru - {len_vac_hh}')

    # with open('hh.json', 'w', encoding='utf8') as f:
    #     json.dump(hh_json, f,  ensure_ascii=False)
    #     f.close()
    #
    # with open('sj.json', 'w', encoding='utf8') as f:
    #     json.dump(sj_json, f, ensure_ascii=False)
    #     f.close()
