from jobs_classes import *


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
                data = json.load(f)
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

    def select(self):
        with open(self.__data_file, 'r', encoding='utf8') as f:
            data = json.load(f)
            f.close()
            return data

    def delete(self, query):
        pass
