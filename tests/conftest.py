import pytest, json


@pytest.fixture()
def test_data_hh():
    with open('hh.json', 'r', encoding='utf8') as f:
        data = json.load(f)
        f.close()
    return data


@pytest.fixture()
def test_data_sj():
    with open('sj.json', 'r', encoding='utf8') as f:
        data = json.load(f)
        f.close()
    return data


@pytest.fixture()
def test_data_hh_sort():
    range_vac_hh = []
    with open('hh.json', 'r', encoding='utf8') as f:
        data = json.load(f)
        f.close()
    for i in range(len(data)):
        if data[i]['salary'] is not None and data[i]['salary']['from'] is not None:
            range_vac_hh.append(data[i])
    range_vac_hh.sort(key=lambda x: x['salary']['from'], reverse=True)
    return range_vac_hh[0]