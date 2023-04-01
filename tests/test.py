from classes import *
from jobs_classes import *
from tests.conftest import *


def test_get_request():
    hhh = HH()
    hhh_json = hhh.get_request('python разработчик')
    hh_connect = hhh.get_connector('hh.json')
    hh_connect.insert(hhh_json)
    dict_hh = hh_connect.select()
    assert print(dict_hh) == print(test_data_hh)


def test_get_req():
    ssj = Superjob()
    ssj_json = ssj.get_request('python разработчик')
    sj_connect = ssj.get_connector('sj.json')
    sj_connect.insert(ssj_json)
    dict_sj = sj_connect.select()
    assert print(dict_sj) == print(test_data_sj)


def test___connect():
    hhh = HH()
    hh_connect = hhh.get_connector('hh.json')
    assert print(hh_connect._Connector__connect()) == print('Файл существует')


def test_CountMixin():
    hhh = HH()
    ssj = Superjob()
    hhh_json = hhh.get_request('python разработчик')
    ssj_json = ssj.get_request('python разработчик')
    vac_test_hh = HHVacancy(hhh_json[0])
    vac_test_sj = SJVacancy(ssj_json[0])
    len_vac_hh = vac_test_hh.get_count_of_vacancy('hh.json')
    len_vac_sj = vac_test_sj.get_count_of_vacancy('sj.json')
    assert len_vac_hh == 100
    assert len_vac_sj == 100


def test_sorting():
    hhh = HH()
    hhh_json = hhh.get_request('python разработчик')
    vac_test_hh = HHVacancy(hhh_json[0])
    hh_connect = hhh.get_connector('hh.json')
    dict_hh = hh_connect.select()
    sort_vac_hh = vac_test_hh.sorting(dict_hh)
    assert print(sort_vac_hh[0]) == print(test_data_hh_sort)


def test_get_top():
    hhh = HH()
    hhh_json = hhh.get_request('python разработчик')
    vac_test_hh = HHVacancy(hhh_json[0])
    hh_connect = hhh.get_connector('hh.json')
    dict_hh = hh_connect.select()
    vac_test_hh.sorting(dict_hh)
    sort_vac_top = vac_test_hh.get_top()
    assert print(sort_vac_top[0]) == print(test_data_hh_sort)
    assert print(sort_vac_top[0]) == print(test_data_hh_sort)
