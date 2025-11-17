import os
from task3.csv_loader import load_table as load_csv, save_table as save_csv
from task3.pickle_loader import load_table as load_pickle, save_table as save_pickle
from task3.text_saver import save_table as save_text
from task3.table_operations import Table
from task3.result_manager import show_result_menu, save_result_menu


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_table_menu():
    print("=" * 60)
    print("           📊 РАБОТА С ТАБЛИЦАМИ")
    print("=" * 60)
    print("Выберите действие:")
    print(" 1. Загрузить таблицу из CSV")
    print(" 2. Загрузить таблицу из Pickle")
    print(" 3. Сохранить таблицу в CSV")
    print(" 4. Сохранить таблицу в Pickle")
    print(" 5. Сохранить таблицу в текстовый файл")
    print(" 6. Показать таблицу")
    print(" 7. Выполнить операции с таблицей")
    print(" 8. Создать пример таблицы")
    print(" 0. Назад в главное меню")
    print("=" * 60)


def display_operations_menu():
    print("=" * 60)
    print("           🔧 ОПЕРАЦИИ С ТАБЛИЦЕЙ")
    print("=" * 60)
    print(" 1. Получить строки по номерам")
    print(" 2. Получить строки по индексу")
    print(" 3. Получить типы столбцов")
    print(" 4. Установить типы столбцов")
    print(" 5. Получить значения столбца")
    print(" 6. Установить значения столбца")
    print(" 7. Арифметические операции")
    print(" 8. Операции сравнения")
    print(" 9. Фильтрация строк")
    print("10. Слияние таблиц")
    print(" 0. Назад")
    print("=" * 60)


def display_arithmetic_menu():
    print("=" * 60)
    print("           ➕ АРИФМЕТИЧЕСКИЕ ОПЕРАЦИИ")
    print("=" * 60)
    print(" 1. Сложение (add)")
    print(" 2. Вычитание (sub)")
    print(" 3. Умножение (mul)")
    print(" 4. Деление (div)")
    print(" 0. Назад")
    print("=" * 60)


def display_comparison_menu():
    print("=" * 60)
    print("           🔄 ОПЕРАЦИИ СРАВНЕНИЯ")
    print("=" * 60)
    print(" 1. Равно (eq)")
    print(" 2. Больше (gr)")
    print(" 3. Меньше (ls)")
    print(" 4. Больше или равно (ge)")
    print(" 5. Меньше или равно (le)")
    print(" 6. Не равно (ne)")
    print(" 0. Назад")
    print("=" * 60)


def get_user_choice(min_val, max_val, prompt="Введите номер: "):
    while True:
        try:
            choice = int(input(prompt))
            if min_val <= choice <= max_val:
                return choice
            else:
                print(f"Пожалуйста, введите число от {min_val} до {max_val}")
        except ValueError:
            print("Пожалуйста, введите корректное число")


def get_column_input(prompt="Введите столбец (имя или номер): "):
    """Получает ввод столбца от пользователя"""
    value = input(prompt).strip()
    try:
        return int(value)
    except ValueError:
        return value


def load_table_from_csv():
    try:
        filename = input("Введите имя CSV файла: ").strip()
        if not filename:
            print("Имя файла не может быть пустым")
            return None

        has_headers = input("Есть заголовки? (y/n, по умолчанию y): ").strip().lower() != 'n'
        delimiter = input("Введите разделитель (по умолчанию ,): ").strip()
        if not delimiter:
            delimiter = ','

        table = load_csv(filename, delimiter=delimiter, has_headers=has_headers)
        print(f"✅ Таблица успешно загружена из {filename}")
        print(f"   Столбцы: {table.headers}")
        print(f"   Строк: {len(table.data)}")
        return table

    except Exception as e:
        print(f"❌ Ошибка загрузки: {e}")
        return None


def load_table_from_pickle():
    try:
        filename = input("Введите имя Pickle файла: ").strip()
        if not filename:
            print("Имя файла не может быть пустым")
            return None

        table = load_pickle(filename)
        print(f"✅ Таблица успешно загружена из {filename}")
        print(f"   Столбцы: {table.headers}")
        print(f"   Строк: {len(table.data)}")
        return table

    except Exception as e:
        print(f"❌ Ошибка загрузки: {e}")
        return None


def save_table_to_csv(table):
    if table is None:
        print("❌ Сначала загрузите таблицу!")
        return

    try:
        filename = input("Введите имя файла для сохранения: ").strip()
        if not filename:
            print("Имя файла не может быть пустым")
            return

        write_headers = input("Записывать заголовки? (y/n, по умолчанию y): ").strip().lower() != 'n'
        delimiter = input("Введите разделитель (по умолчанию ,): ").strip()
        if not delimiter:
            delimiter = ','

        save_csv(table, filename, delimiter=delimiter, write_headers=write_headers)
        print(f"✅ Таблица успешно сохранена в {filename}")

    except Exception as e:
        print(f"❌ Ошибка сохранения: {e}")


def save_table_to_pickle(table):
    if table is None:
        print("❌ Сначала загрузите таблицу!")
        return

    try:
        filename = input("Введите имя файла для сохранения: ").strip()
        if not filename:
            print("Имя файла не может быть пустым")
            return

        save_pickle(table, filename)
        print(f"✅ Таблица успешно сохранена в {filename}")

    except Exception as e:
        print(f"❌ Ошибка сохранения: {e}")


def save_table_to_text(table):
    if table is None:
        print("❌ Сначала загрузите таблицу!")
        return

    try:
        filename = input("Введите имя файла для сохранения: ").strip()
        if not filename:
            print("Имя файла не может быть пустым")
            return

        save_text(table, filename)
        print(f"✅ Таблица успешно сохранена в {filename}")

    except Exception as e:
        print(f"❌ Ошибка сохранения: {e}")


def show_table(table):
    if table is None:
        print("❌ Сначала загрузите таблицу!")
        return

    try:
        print("\n" + "=" * 80)
        table.print_table()
        print("=" * 80)
    except Exception as e:
        print(f"❌ Ошибка отображения: {e}")


def create_sample_table():
    """Создает пример таблицы для демонстрации"""
    sample_data = [
        [1, "Иван", 25, 75000.50, True],
        [2, "Мария", 30, 80000.75, False],
        [3, "Петр", 35, 90000.25, True],
        [4, "Анна", 28, 85000.00, True],
        [5, "Сергей", 40, 95000.50, False]
    ]
    headers = ["ID", "Имя", "Возраст", "Зарплата", "Активен"]

    table = Table(sample_data, headers)
    print("✅ Создана примерная таблица:")
    table.print_table()
    return table


def operations_get_rows_by_number(table):
    """Операция получения строк по номерам - БЕЗ автоматического применения"""
    try:
        start = int(input("Введите начальный номер строки: "))
        stop_input = input("Введите конечный номер строки (Enter если одна строка): ").strip()
        stop = int(stop_input) if stop_input else None
        copy_table = input("Копировать данные? (y/n, по умолчанию n): ").strip().lower() == 'y'

        result = table.get_rows_by_number(start, stop, copy_table)
        return result, "ПОЛУЧЕНИЕ СТРОК ПО НОМЕРАМ"

    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return table, None


def operations_get_rows_by_index(table):
    """Операция получения строк по индексу - БЕЗ автоматического применения"""
    try:
        values_input = input("Введите значения для поиска (через пробел): ").strip()
        values = [v.strip() for v in values_input.split()]
        copy_table = input("Копировать данные? (y/n, по умолчанию n): ").strip().lower() == 'y'

        result = table.get_rows_by_index(*values, copy_table=copy_table)
        return result, "ПОЛУЧЕНИЕ СТРОК ПО ИНДЕКСУ"

    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return table, None


def operations_get_column_types(table):
    """Операция получения типов столбцов"""
    try:
        by_number = input("Использовать номера столбцов? (y/n, по умолчанию y): ").strip().lower() != 'n'
        types = table.get_column_types(by_number)
        print("\n📊 Типы столбцов:")
        for col, col_type in types.items():
            print(f"  {col}: {col_type}")
    except Exception as e:
        print(f"❌ Ошибка: {e}")


def operations_set_column_types(table):
    """Операция установки типов столбцов"""
    try:
        by_number = input("Использовать номера столбцов? (y/n, по умолчанию y): ").strip().lower() != 'n'
        print("Введите типы столбцов в формате: столбец=тип")
        print("Доступные типы: int, float, bool, str")
        print("Пример: 0=int или 'Имя'=str")
        print("Введите 'done' для завершения:")

        types_dict = {}
        while True:
            input_str = input("> ").strip()
            if input_str.lower() == 'done':
                break
            if '=' in input_str:
                key, value = input_str.split('=', 1)
                key = key.strip()
                # Обрабатываем ключ
                if key.startswith("'") and key.endswith("'") or key.startswith('"') and key.endswith('"'):
                    key = key[1:-1]
                else:
                    try:
                        key = int(key)
                    except ValueError:
                        pass
                types_dict[key] = value.strip()

        table.set_column_types(types_dict, by_number)
        print("✅ Типы столбцов успешно установлены")

    except Exception as e:
        print(f"❌ Ошибка: {e}")


def operations_get_values(table):
    """Операция получения значений столбца"""
    try:
        column = get_column_input("Введите столбец: ")
        values = table.get_values(column)
        print(f"\n📋 Значения столбца {column}:")
        for i, value in enumerate(values):
            print(f"  Строка {i}: {value} ({type(value).__name__})")
    except Exception as e:
        print(f"❌ Ошибка: {e}")


def operations_set_values(table):
    """Операция установки значений столбца"""
    try:
        column = get_column_input("Введите столбец: ")
        print("Введите значения (по одному в строке, 'done' для завершения):")
        values = []
        while True:
            value_str = input(f"Значение {len(values)}: ").strip()
            if value_str.lower() == 'done':
                break
            values.append(value_str)

        table.set_values(values, column)
        print("✅ Значения успешно установлены")

    except Exception as e:
        print(f"❌ Ошибка: {e}")


def arithmetic_operations(table):
    """Меню арифметических операций - работают напрямую с таблицей"""
    if table is None:
        print("❌ Сначала загрузите таблицу!")
        return

    while True:
        clear_screen()
        display_arithmetic_menu()
        choice = get_user_choice(0, 4)

        if choice == 0:
            break

        try:
            col1 = get_column_input("Введите первый столбец: ")
            col2 = get_column_input("Введите второй столбец: ")
            result_col = get_column_input("Введите столбец для результата: ")

            if choice == 1:
                table.add(col1, col2, result_col)
                print("✅ Сложение выполнено")
            elif choice == 2:
                table.sub(col1, col2, result_col)
                print("✅ Вычитание выполнено")
            elif choice == 3:
                table.mul(col1, col2, result_col)
                print("✅ Умножение выполнено")
            elif choice == 4:
                table.div(col1, col2, result_col)
                print("✅ Деление выполнено")

            input("\nНажмите Enter чтобы продолжить...")

        except Exception as e:
            print(f"❌ Ошибка: {e}")
            input("\nНажмите Enter чтобы продолжить...")


def comparison_operations(table):
    """Меню операций сравнения - работают напрямую с таблицей"""
    if table is None:
        print("❌ Сначала загрузите таблицу!")
        return

    while True:
        clear_screen()
        display_comparison_menu()
        choice = get_user_choice(0, 6)

        if choice == 0:
            break

        try:
            col1 = get_column_input("Введите первый столбец: ")
            col2 = get_column_input("Введите второй столбец: ")

            if choice == 1:
                result = table.eq(col1, col2)
                print("✅ Результат сравнения (==):", result)
            elif choice == 2:
                result = table.gr(col1, col2)
                print("✅ Результат сравнения (>):", result)
            elif choice == 3:
                result = table.ls(col1, col2)
                print("✅ Результат сравнения (<):", result)
            elif choice == 4:
                result = table.ge(col1, col2)
                print("✅ Результат сравнения (>=):", result)
            elif choice == 5:
                result = table.le(col1, col2)
                print("✅ Результат сравнения (<=):", result)
            elif choice == 6:
                result = table.ne(col1, col2)
                print("✅ Результат сравнения (!=):", result)

            # Предлагаем фильтрацию
            if input("Выполнить фильтрацию по результату? (y/n): ").strip().lower() == 'y':
                copy_table = input("Копировать данные? (y/n): ").strip().lower() == 'y'
                filtered = table.filter_rows(result, copy_table)

                # Для фильтрации тоже используем меню подтверждения
                from task3.result_manager import show_result_menu, save_result_menu
                operation_choice = show_result_menu(table, filtered, "ФИЛЬТРАЦИЯ ПО СРАВНЕНИЮ")

                if operation_choice == 1:
                    table = filtered
                    print("✅ Таблица заменена результатом фильтрации")
                elif operation_choice == 2:
                    save_result_menu(filtered)
                # choice == 3 - продолжаем с исходной таблицей

            input("\nНажмите Enter чтобы продолжить...")

        except Exception as e:
            print(f"❌ Ошибка: {e}")
            input("\nНажмите Enter чтобы продолжить...")


def filter_rows_operation(table):
    """Операция фильтрации строк - БЕЗ автоматического применения"""
    try:
        print("Введите булевские значения (True/False) для каждой строки:")
        print(f"Всего строк: {len(table.data)}")
        bool_list = []
        for i in range(len(table.data)):
            while True:
                value = input(f"Строка {i} (True/False): ").strip().lower()
                if value in ('true', 't', '1', 'y', 'yes'):
                    bool_list.append(True)
                    break
                elif value in ('false', 'f', '0', 'n', 'no'):
                    bool_list.append(False)
                    break
                else:
                    print("Пожалуйста, введите True или False")

        copy_table = input("Копировать данные? (y/n): ").strip().lower() == 'y'
        result = table.filter_rows(bool_list, copy_table)
        return result, "ФИЛЬТРАЦИЯ СТРОК"

    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return table, None


def merge_tables_operation(table):
    """Операция слияния таблиц - БЕЗ автоматического применения"""
    try:
        print("Для слияния нужна вторая таблица.")
        print("1. Загрузить вторую таблицу из CSV")
        print("2. Загрузить вторую таблицу из Pickle")
        print("3. Создать примерную таблицу")
        choice = get_user_choice(1, 3)

        if choice == 1:
            table2 = load_table_from_csv()
        elif choice == 2:
            table2 = load_table_from_pickle()
        else:
            table2 = create_sample_table()

        if table2 is None:
            print("❌ Не удалось загрузить вторую таблицу")
            return table, None

        by_number = input("Слияние по номерам строк? (y/n, по умолчанию y): ").strip().lower() != 'n'
        conflict = input("Стратегия разрешения конфликтов (raise/table1/table2, по умолчанию raise): ").strip()
        if not conflict:
            conflict = 'raise'

        result = Table.merge_tables(table, table2, by_number, conflict)
        return result, "СЛИЯНИЕ ТАБЛИЦ"

    except Exception as e:
        print(f"❌ Ошибка слияния: {e}")
        return table, None


def handle_operation_result(original_table, result_table, operation_name):
    """Обрабатывает результат операции и спрашивает пользователя что делать"""
    if result_table is original_table or operation_name is None:
        return original_table  # Операция не выполнена или результат = исходнику

    while True:
        choice = show_result_menu(original_table, result_table, operation_name)

        if choice == 1:
            # ЗАМЕНИТЬ исходную таблицу
            print("✅ Исходная таблица заменена результатом")
            input("\nНажмите Enter чтобы продолжить...")
            return result_table

        elif choice == 2:
            # Сохранить результат
            save_result_menu(result_table)
            # После сохранения снова показываем меню выбора
            continue

        elif choice == 3:
            # Продолжить с исходной таблицей
            print("✅ Возврат к исходной таблице")
            input("\nНажмите Enter чтобы продолжить...")
            return original_table

        elif choice == 0:
            # Временно сохранить результат (для цепочки операций)
            return result_table


def handle_operation_result(original_table, result_table, operation_name):
    """Обрабатывает результат операции и спрашивает пользователя что делать"""
    if result_table is original_table or operation_name is None:
        return original_table  # Операция не выполнена или результат = исходнику

    while True:
        choice = show_result_menu(original_table, result_table, operation_name)

        if choice == 1:
            # ЗАМЕНИТЬ исходную таблицу
            print("✅ Исходная таблица заменена результатом")
            input("\nНажмите Enter чтобы продолжить...")
            return result_table

        elif choice == 2:
            # Сохранить результат
            save_result_menu(result_table)
            # После сохранения снова показываем меню выбора
            continue

        elif choice == 3:
            # Продолжить с исходной таблицей
            print("✅ Возврат к исходной таблице")
            input("\nНажмите Enter чтобы продолжить...")
            return original_table

        elif choice == 0:
            # Временно сохранить результат (для цепочки операций)
            return result_table


def operations_menu(current_table):
    """Главное меню операций с таблицами - ПЕРЕРАБОТАННАЯ"""
    table = current_table

    while True:
        clear_screen()
        if table:
            print(f"📊 Текущая таблица: {len(table.data)} строк, {len(table.headers)} столбцов")
        display_operations_menu()
        choice = get_user_choice(0, 10)

        if choice == 0:
            break

        # Операции, которые МЕНЯЮТ таблицу и требуют подтверждения
        elif choice in [1, 2, 9, 10]:
            result_table = table
            operation_name = None

            if choice == 1:
                result_table, operation_name = operations_get_rows_by_number(table)
            elif choice == 2:
                result_table, operation_name = operations_get_rows_by_index(table)
            elif choice == 9:
                result_table, operation_name = filter_rows_operation(table)
            elif choice == 10:
                result_table, operation_name = merge_tables_operation(table)

            # Обрабатываем результат операции
            if operation_name:
                table = handle_operation_result(table, result_table, operation_name)

        # Операции, которые НЕ меняют таблицу (работают напрямую)
        elif choice == 3:
            operations_get_column_types(table)
            input("\nНажмите Enter чтобы продолжить...")
        elif choice == 4:
            operations_set_column_types(table)
            input("\nНажмите Enter чтобы продолжить...")
        elif choice == 5:
            operations_get_values(table)
            input("\nНажмите Enter чтобы продолжить...")
        elif choice == 6:
            operations_set_values(table)
            input("\nНажмите Enter чтобы продолжить...")
        elif choice == 7:
            arithmetic_operations(table)
        elif choice == 8:
            comparison_operations(table)

    return table


def play():
    """Основная функция для работы с таблицами"""
    current_table = None

    while True:
        clear_screen()
        display_table_menu()
        choice = get_user_choice(0, 8)

        if choice == 0:
            break
        elif choice == 1:
            current_table = load_table_from_csv()
        elif choice == 2:
            current_table = load_table_from_pickle()
        elif choice == 3:
            save_table_to_csv(current_table)
        elif choice == 4:
            save_table_to_pickle(current_table)
        elif choice == 5:
            save_table_to_text(current_table)
        elif choice == 6:
            show_table(current_table)
        elif choice == 7:
            current_table = operations_menu(current_table)
        elif choice == 8:
            current_table = create_sample_table()

        if choice != 0:
            input("\nНажмите Enter чтобы продолжить...")