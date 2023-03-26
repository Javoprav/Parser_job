from classes import *
from jobs_classes import *


hh = HH()
sj = Superjob()
if __name__ == '__main__':
    user_input = input('Введите название вакансии: ')
    hh_json = hh.get_request(user_input)
    sj_json = sj.get_request(user_input)
    hh_connect = hh.get_connector('hh.json')
    sj_connect = sj.get_connector('sj.json')
    hh_connect.insert(hh_json)
    sj_connect.insert(sj_json)
    vac_test_hh = HHVacancy(hh_json[0])
    vac_test_sj = SJVacancy(sj_json[0])
    # pprint(sj_json[0])
    # pprint(vac_test_sj)
    len_vac_hh = vac_test_hh.get_count_of_vacancy('hh.json')
    len_vac_sj = vac_test_sj.get_count_of_vacancy('sj.json')
    print(f'Собрано вакансий с сайта hh.ru - {len_vac_hh} и записаны в файл "hh.json"')
    print(f'Собрано вакансий с сайта superjob.ru - {len_vac_sj} и записаны в файл "sj.json"')
    user_input2 = input(f'-- Если хотите увидеть все вакансии с сайта hh.ru введите "hh", '
                        f'\n-- Если хотите увидеть все вакансии с сайта superjob.ru введите "sj", '
                        f'\n-- Если хотите отсортировать по зарплате вакансии с сайта hh.ru введите "sort-hh" или '
                        f'"sort-sj",'
                        f'\n-- Если хотите увидеть Top-10 вакансии с сайта hh.ru введите "Top-hh" или "Top-sj", '
                        f'\n-- если хотите выйти напишите "stop" или любую букву: ')
    dict_hh = hh_connect.select()
    dict_sj = sj_connect.select()
    if user_input2.lower() == 'hh':
        all_vac_hh = []
        for i in range(len(dict_hh)):
            vacancy = HHVacancy(dict_hh[i])
            all_vac_hh.append(vacancy)
        for x in all_vac_hh:
            print(x)
    elif user_input2.lower() == 'sj':
        all_vac_sj = []
        for i in range(len(dict_sj)):
            vacancy = SJVacancy(dict_sj[i])
            all_vac_sj.append(vacancy)
        for x in all_vac_sj:
            print(x)
    elif user_input2.lower() == "sort-hh":
        sort_vac_hh = vac_test_hh.sorting(dict_hh)
        all_vac_sort_hh = []
        for i in range(len(sort_vac_hh)):
            vacancy = HHVacancy(sort_vac_hh[i])
            all_vac_sort_hh.append(vacancy)
        for x in all_vac_sort_hh:
            print(x)
    elif user_input2.lower() == "sort-sj":
        sort_vac_sj = vac_test_sj.sorting(dict_sj)
        all_vac_sort_sj = []
        for i in range(len(sort_vac_sj)):
            vacancy = SJVacancy(sort_vac_sj[i])
            all_vac_sort_sj.append(vacancy)
        for x in all_vac_sort_sj:
            print(x)
    elif user_input2.lower() == "top-hh":
        sort_vac_hh = vac_test_hh.sorting(dict_hh)
        sort_vac_top = vac_test_hh.get_top()
        for x in sort_vac_top:
            print(x)
    elif user_input2.lower() == "top-sj":
        sort_vac_sj = vac_test_sj.sorting(dict_sj)
        sort_vac_top = vac_test_sj.get_top()
        for x in sort_vac_top:
            print(x)
    elif user_input2.lower() == 'stop':
        print("Выход!")
        exit()
    else:
        print("Не верный ввод! Выход!")
        exit()
