from task3.exceptions import *


class Table:
    """Класс для представления таблицы"""

    def __init__(self, data=None, headers=None):
        self.data = data or []
        self.headers = headers or []
        self.column_types = {}
        self._auto_detect_types()

    def _auto_detect_types(self):
        """Автоматическое определение типов столбцов"""
        if not self.data:
            return

        for col_idx in range(len(self.headers)):
            values = [row[col_idx] for row in self.data if col_idx < len(row)]
            if not values:
                self.column_types[col_idx] = str
                continue

            # Пробуем определить тип
            sample_value = values[0]
            if isinstance(sample_value, (int, float, bool, str)):
                self.column_types[col_idx] = type(sample_value)
            else:
                self.column_types[col_idx] = str

    def _convert_value(self, value, col_idx):
        """Конвертирует значение к типу столбца"""
        col_type = self.column_types.get(col_idx, str)
        try:
            if col_type == bool:
                if isinstance(value, str):
                    return value.lower() in ('true', '1', 'yes', 'y')
                return bool(value)
            elif col_type == int:
                return int(value)
            elif col_type == float:
                return float(value)
            else:
                return str(value)
        except (ValueError, TypeError):
            raise TypeError(f"Не удалось конвертировать {value} в {col_type.__name__}")

    def get_rows_by_number(self, start, stop=None, copy_table=False):
        """Получение строк по номерам"""
        if not self.data:
            raise RowError("Таблица пуста")

        if start < 0 or start >= len(self.data):
            raise RowError(f"Некорректный начальный индекс: {start}")

        if stop is not None and (stop < 0 or stop > len(self.data)):
            raise RowError(f"Некорректный конечный индекс: {stop}")

        if stop is None:
            selected_data = [self.data[start]]
        else:
            selected_data = self.data[start:stop]

        if copy_table:
            # Глубокая копия
            import copy
            new_data = copy.deepcopy(selected_data)
            new_headers = copy.deepcopy(self.headers)
            new_types = self.column_types.copy()
            new_table = Table(new_data, new_headers)
            new_table.column_types = new_types
            return new_table
        else:
            # Представление на исходных данных
            new_table = Table(selected_data, self.headers)
            new_table.column_types = self.column_types
            return new_table

    def get_rows_by_index(self, *values, copy_table=False):
        """Получение строк по значениям в первом столбце"""
        if not self.data:
            raise RowError("Таблица пуста")

        if not values:
            raise RowError("Не указаны значения для поиска")

        selected_data = []
        for row in self.data:
            if row and len(row) > 0:
                first_val = self._convert_value(row[0], 0)
                if first_val in values:
                    selected_data.append(row)

        if not selected_data:
            raise RowError("Не найдено строк с указанными значениями")

        if copy_table:
            import copy
            new_data = copy.deepcopy(selected_data)
            new_headers = copy.deepcopy(self.headers)
            new_types = self.column_types.copy()
            new_table = Table(new_data, new_headers)
            new_table.column_types = new_types
            return new_table
        else:
            new_table = Table(selected_data, self.headers)
            new_table.column_types = self.column_types
            return new_table

    def get_column_types(self, by_number=True):
        """Получение типов столбцов"""
        result = {}
        for col_idx, col_type in self.column_types.items():
            key = col_idx if by_number else self.headers[col_idx]
            result[key] = col_type.__name__
        return result

    def set_column_types(self, types_dict, by_number=True):
        """Установка типов столбцов"""
        for key, type_str in types_dict.items():
            if by_number:
                col_idx = key
            else:
                if key not in self.headers:
                    raise ColumnError(f"Столбец '{key}' не найден")
                col_idx = self.headers.index(key)

            # Преобразуем строку в тип
            if type_str == 'int':
                new_type = int
            elif type_str == 'float':
                new_type = float
            elif type_str == 'bool':
                new_type = bool
            elif type_str == 'str':
                new_type = str
            else:
                raise TypeError(f"Неподдерживаемый тип: {type_str}")

            self.column_types[col_idx] = new_type

            # Конвертируем существующие значения
            for row in self.data:
                if col_idx < len(row):
                    row[col_idx] = self._convert_value(row[col_idx], col_idx)

    def get_values(self, column=0):
        """Получение значений столбца"""
        if isinstance(column, str):
            if column not in self.headers:
                raise ColumnError(f"Столбец '{column}' не найден")
            col_idx = self.headers.index(column)
        else:
            col_idx = column

        if col_idx < 0 or col_idx >= len(self.headers):
            raise ColumnError(f"Некорректный индекс столбца: {col_idx}")

        values = []
        for row in self.data:
            if col_idx < len(row):
                values.append(self._convert_value(row[col_idx], col_idx))
            else:
                values.append(None)
        return values

    def get_value(self, column=0):
        """Получение значения из таблицы с одной строкой"""
        if len(self.data) != 1:
            raise RowError("Метод get_value предназначен для таблиц с одной строкой")
        values = self.get_values(column)
        return values[0] if values else None

    def set_values(self, values, column=0):
        """Установка значений столбца"""
        if isinstance(column, str):
            if column not in self.headers:
                raise ColumnError(f"Столбец '{column}' не найден")
            col_idx = self.headers.index(column)
        else:
            col_idx = column

        if col_idx < 0 or col_idx >= len(self.headers):
            raise ColumnError(f"Некорректный индекс столбца: {col_idx}")

        if len(values) != len(self.data):
            raise ColumnError("Количество значений должно совпадать с количеством строк")

        for i, value in enumerate(values):
            if col_idx >= len(self.data[i]):
                self.data[i].extend([None] * (col_idx - len(self.data[i]) + 1))
            self.data[i][col_idx] = self._convert_value(value, col_idx)

    def set_value(self, value, column=0):
        """Установка значения в таблице с одной строкой"""
        if len(self.data) != 1:
            raise RowError("Метод set_value предназначен для таблиц с одной строкой")
        self.set_values([value], column)

    def print_table(self):
        """Вывод таблицы на печать"""
        if not self.headers and not self.data:
            print("Таблица пуста")
            return

        # Определяем ширину столбцов
        col_widths = []
        for i, header in enumerate(self.headers):
            max_width = len(str(header))
            for row in self.data:
                if i < len(row):
                    max_width = max(max_width, len(str(row[i])))
            col_widths.append(max_width + 2)

        # Вывод заголовков
        header_line = "|"
        for i, header in enumerate(self.headers):
            header_line += f" {str(header):<{col_widths[i]}} |"
        print(header_line)

        # Разделитель
        separator = "+"
        for width in col_widths:
            separator += "-" * (width + 2) + "+"
        print(separator)

        # Вывод данных
        for row in self.data:
            row_line = "|"
            for i in range(len(self.headers)):
                if i < len(row):
                    value = str(row[i])
                else:
                    value = ""
                row_line += f" {value:<{col_widths[i]}} |"
            print(row_line)

    # Арифметические операции
    def _check_numeric_operation(self, col1, col2):
        """Проверка возможности арифметической операции"""
        values1 = self.get_values(col1)
        values2 = self.get_values(col2)

        for val1, val2 in zip(values1, values2):
            if not isinstance(val1, (int, float)) or not isinstance(val2, (int, float)):
                raise OperationError("Арифметические операции возможны только для числовых столбцов")
        return values1, values2

    def add(self, col1, col2, result_col):
        """Сложение столбцов"""
        values1, values2 = self._check_numeric_operation(col1, col2)
        result_values = [v1 + v2 for v1, v2 in zip(values1, values2)]
        self.set_values(result_values, result_col)

    def sub(self, col1, col2, result_col):
        """Вычитание столбцов"""
        values1, values2 = self._check_numeric_operation(col1, col2)
        result_values = [v1 - v2 for v1, v2 in zip(values1, values2)]
        self.set_values(result_values, result_col)

    def mul(self, col1, col2, result_col):
        """Умножение столбцов"""
        values1, values2 = self._check_numeric_operation(col1, col2)
        result_values = [v1 * v2 for v1, v2 in zip(values1, values2)]
        self.set_values(result_values, result_col)

    def div(self, col1, col2, result_col):
        """Деление столбцов"""
        values1, values2 = self._check_numeric_operation(col1, col2)
        result_values = []
        for v1, v2 in zip(values1, values2):
            if v2 == 0:
                raise OperationError("Деление на ноль")
            result_values.append(v1 / v2)
        self.set_values(result_values, result_col)

    # Операции сравнения
    def _compare_columns(self, col1, col2, operation):
        """Базовый метод для операций сравнения"""
        values1 = self.get_values(col1)
        values2 = self.get_values(col2)

        if len(values1) != len(values2):
            raise OperationError("Столбцы должны иметь одинаковую длину")

        operations = {
            'eq': lambda x, y: x == y,
            'gr': lambda x, y: x > y,
            'ls': lambda x, y: x < y,
            'ge': lambda x, y: x >= y,
            'le': lambda x, y: x <= y,
            'ne': lambda x, y: x != y
        }

        return [operations[operation](v1, v2) for v1, v2 in zip(values1, values2)]

    def eq(self, col1, col2):
        return self._compare_columns(col1, col2, 'eq')

    def gr(self, col1, col2):
        return self._compare_columns(col1, col2, 'gr')

    def ls(self, col1, col2):
        return self._compare_columns(col1, col2, 'ls')

    def ge(self, col1, col2):
        return self._compare_columns(col1, col2, 'ge')

    def le(self, col1, col2):
        return self._compare_columns(col1, col2, 'le')

    def ne(self, col1, col2):
        return self._compare_columns(col1, col2, 'ne')

    def filter_rows(self, bool_list, copy_table=False):
        """Фильтрация строк по булевскому списку"""
        if len(bool_list) != len(self.data):
            raise RowError("Длина bool_list должна совпадать с количеством строк")

        filtered_data = [row for i, row in enumerate(self.data) if bool_list[i]]

        if copy_table:
            import copy
            new_data = copy.deepcopy(filtered_data)
            new_headers = copy.deepcopy(self.headers)
            new_types = self.column_types.copy()
            new_table = Table(new_data, new_headers)
            new_table.column_types = new_types
            return new_table
        else:
            new_table = Table(filtered_data, self.headers)
            new_table.column_types = self.column_types
            return new_table

    @staticmethod
    def merge_tables(table1, table2, by_number=True, conflict_resolution='raise'):
        """
        Слияние таблиц

        Параметры:
        - conflict_resolution: 'raise' - вызвать исключение, 
                              'table1' - использовать значения из table1,
                              'table2' - использовать значения из table2
        """
        if conflict_resolution not in ('raise', 'table1', 'table2'):
            raise MergeError("Некорректная стратегия разрешения конфликтов")

        # Объединяем заголовки
        all_headers = table1.headers.copy()
        for header in table2.headers:
            if header not in all_headers:
                all_headers.append(header)

        merged_data = []

        if by_number:
            # Слияние по номерам строк
            max_rows = max(len(table1.data), len(table2.data))

            for i in range(max_rows):
                merged_row = []

                for header in all_headers:
                    if header in table1.headers and header in table2.headers:
                        # Конфликт имен столбцов
                        col1_idx = table1.headers.index(header)
                        col2_idx = table2.headers.index(header)

                        if i < len(table1.data) and i < len(table2.data):
                            val1 = table1.data[i][col1_idx] if col1_idx < len(table1.data[i]) else None
                            val2 = table2.data[i][col2_idx] if col2_idx < len(table2.data[i]) else None

                            if val1 is not None and val2 is not None and val1 != val2:
                                if conflict_resolution == 'raise':
                                    raise MergeError(f"Конфликт значений в строке {i}, столбец '{header}'")
                                elif conflict_resolution == 'table1':
                                    merged_row.append(val1)
                                else:
                                    merged_row.append(val2)
                            else:
                                merged_row.append(val1 or val2)
                        elif i < len(table1.data):
                            merged_row.append(table1.data[i][col1_idx] if col1_idx < len(table1.data[i]) else None)
                        else:
                            merged_row.append(table2.data[i][col2_idx] if col2_idx < len(table2.data[i]) else None)

                    elif header in table1.headers:
                        col_idx = table1.headers.index(header)
                        merged_row.append(
                            table1.data[i][col_idx] if i < len(table1.data) and col_idx < len(table1.data[i]) else None)

                    else:
                        col_idx = table2.headers.index(header)
                        merged_row.append(
                            table2.data[i][col_idx] if i < len(table2.data) and col_idx < len(table2.data[i]) else None)

                merged_data.append(merged_row)

        else:
            # Слияние по значениям первого столбца (индексу)
            index_dict1 = {}
            for row in table1.data:
                if row:
                    index_dict1[str(row[0])] = row

            index_dict2 = {}
            for row in table2.data:
                if row:
                    index_dict2[str(row[0])] = row

            all_indices = set(index_dict1.keys()) | set(index_dict2.keys())

            for index in sorted(all_indices):
                merged_row = []
                row1 = index_dict1.get(index, [])
                row2 = index_dict2.get(index, [])

                for header in all_headers:
                    if header in table1.headers and header in table2.headers:
                        col1_idx = table1.headers.index(header)
                        col2_idx = table2.headers.index(header)

                        val1 = row1[col1_idx] if row1 and col1_idx < len(row1) else None
                        val2 = row2[col2_idx] if row2 and col2_idx < len(row2) else None

                        if val1 is not None and val2 is not None and val1 != val2:
                            if conflict_resolution == 'raise':
                                raise MergeError(f"Конфликт значений для индекса {index}, столбец '{header}'")
                            elif conflict_resolution == 'table1':
                                merged_row.append(val1)
                            else:
                                merged_row.append(val2)
                        else:
                            merged_row.append(val1 or val2)

                    elif header in table1.headers:
                        col_idx = table1.headers.index(header)
                        merged_row.append(row1[col_idx] if row1 and col_idx < len(row1) else None)

                    else:
                        col_idx = table2.headers.index(header)
                        merged_row.append(row2[col_idx] if row2 and col_idx < len(row2) else None)

                merged_data.append(merged_row)

        merged_table = Table(merged_data, all_headers)

        # Объединяем типы столбцов
        for col_idx, header in enumerate(all_headers):
            if header in table1.headers:
                orig_idx = table1.headers.index(header)
                if orig_idx in table1.column_types:
                    merged_table.column_types[col_idx] = table1.column_types[orig_idx]
            elif header in table2.headers:
                orig_idx = table2.headers.index(header)
                if orig_idx in table2.column_types:
                    merged_table.column_types[col_idx] = table2.column_types[orig_idx]

        return merged_table