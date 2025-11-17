import pickle
from task3.exceptions import LoadError, SaveError
from task3.table_operations import Table


def load_table(filename):
    """
    Загрузка таблицы из Pickle файла
    """
    try:
        with open(filename, 'rb') as file:
            data = pickle.load(file)

            if isinstance(data, Table):
                return data
            elif isinstance(data, dict) and 'data' in data and 'headers' in data:
                return Table(data['data'], data['headers'])
            else:
                raise LoadError("Некорректный формат данных в Pickle файле")

    except FileNotFoundError:
        raise LoadError(f"Файл {filename} не найден")
    except Exception as e:
        raise LoadError(f"Ошибка загрузки Pickle: {str(e)}")


def save_table(table, filename):
    """
    Сохранение таблицы в Pickle файл
    """
    try:
        with open(filename, 'wb') as file:
            # Сохраняем весь объект Table
            pickle.dump(table, file)

    except Exception as e:
        raise SaveError(f"Ошибка сохранения Pickle: {str(e)}")