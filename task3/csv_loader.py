import csv
from task3.exceptions import LoadError, SaveError
from task3.table_operations import Table


def load_table(filename, delimiter=',', has_headers=True):
    """
    Загрузка таблицы из CSV файла

    Args:
        filename: имя файла
        delimiter: разделитель
        has_headers: есть ли заголовки в первой строке
    """
    try:
        with open(filename, 'r', encoding='utf-8', newline='') as file:
            reader = csv.reader(file, delimiter=delimiter)
            rows = list(reader)

            if not rows:
                raise LoadError("CSV файл пуст")

            if has_headers:
                headers = rows[0]
                data = rows[1:]
            else:
                headers = [f"Column_{i}" for i in range(len(rows[0]))]
                data = rows

            # Преобразуем пустые строки в None
            for i in range(len(data)):
                data[i] = [cell if cell.strip() != '' else None for cell in data[i]]

            return Table(data, headers)

    except FileNotFoundError:
        raise LoadError(f"Файл {filename} не найден")
    except Exception as e:
        raise LoadError(f"Ошибка загрузки CSV: {str(e)}")


def save_table(table, filename, delimiter=',', write_headers=True):
    """
    Сохранение таблицы в CSV файл

    Args:
        table: объект Table
        filename: имя файла
        delimiter: разделитель
        write_headers: записывать ли заголовки
    """
    try:
        with open(filename, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=delimiter)

            if write_headers and table.headers:
                writer.writerow(table.headers)

            for row in table.data:
                # Заменяем None на пустые строки
                cleaned_row = ['' if cell is None else str(cell) for cell in row]
                writer.writerow(cleaned_row)

    except Exception as e:
        raise SaveError(f"Ошибка сохранения CSV: {str(e)}")