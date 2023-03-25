import json


class Connector:
    """
    Класс коннектор к файлу, в json формате
    проверка файла с данными на деградацию
    """
    def __init__(self, file):
        self.__data_file = file

    @property
    def data_file(self):
        """Возврат файла"""
        return self.__data_file

    @data_file.setter
    def data_file(self, value):
        """Установка файла"""
        self.__data_file = value

    def __connect(self):
        """
        Проверка на существование файла
        Также проверить на деградацию
        """
        try:
            with open(self.__data_file, encoding='utf-8') as f:
                data = json.loads(f)
                if data:
                    return 'Файл существует'
        except AttributeError:
            return 'Файла нет'

    def insert(self, data):
        """
        Запись данных в файл с сохранением структуры и исходных данных
        """
        with open(self.__data_file, 'w', encoding='utf8') as f:
            # f.write(str(data))
            json.dump(data, f, ensure_ascii=False)
            f.close()

    def select(self, query):
        """
        Выбор данных из файла с применением фильтрации
        query содержит словарь, в котором ключ это поле для
        фильтрации, а значение это искомое значение, например:
        {'price': 1000}, должно отфильтровать данные по полю price
        и вернуть все строки, в которых цена 1000
        """
        pass

    def delete(self, query):
        pass


if __name__ == '__main__':
    df = Connector('df.json')

    data_for_file = {'id': 1, 'title': 'tet'}

    df.insert(data_for_file)
    data_from_file = df.select(dict())
    assert data_from_file == [data_for_file]

    df.delete({'id':1})
    data_from_file = df.select(dict())
    assert data_from_file == []
