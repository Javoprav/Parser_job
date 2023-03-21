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
    vac_test_hh = HHVacancy(hh_json[0])
    vac_test_sj = SJVacancy(sj_json[0])
    len_vac_hh = vac_test_hh.get_count_of_vacancy('hh.json')
    len_vac_sj = vac_test_sj.get_count_of_vacancy('sj.json')
    print(f'Собрано вакансий с сайта hh.ru - {len_vac_hh} и записаны в файл "hh.json"')
    print(f'Собрано вакансий с сайта superjob.ru - {len_vac_sj} и записаны в файл "sj.json"')
    user_input2 = input(f'Если хотите увидеть все \nвакансии с сайта hh.ru введите "hh", \nс сайта superjob.ru введите "sj", \nесли хотите выйти напишите "stop" или любую букву: ')
    if user_input2.lower() == 'hh':
        all_vac_hh = []
        for i in range(len(hh_json)):
            vacancy = HHVacancy(hh_json[i])
            all_vac_hh.append(vacancy)
        print(all_vac_hh)
    elif user_input2.lower() == 'sj':
        all_vac_sj = []
        for i in range(len(sj_json)):
            vacancy = SJVacancy(sj_json[i])
            all_vac_sj.append(vacancy)
        print(all_vac_sj)
    elif user_input2.lower() == 'stop':
        print("Выход!")
        exit()
    else:
        print("Не верный ввод! Выход!")
        exit()

    # with open('hh.json', 'w', encoding='utf8') as f:
    #     json.dump(hh_json, f,  ensure_ascii=False)
    #     f.close()
    #
    # with open('sj.json', 'w', encoding='utf8') as f:
    #     json.dump(sj_json, f, ensure_ascii=False)
    #     f.close()
