import os
from task3.csv_loader import save_table as save_csv
from task3.pickle_loader import save_table as save_pickle
from task3.text_saver import save_table as save_text


def show_result_menu(original_table, result_table, operation_name):
    """Показывает меню управления результатом операции"""
    clear_screen()

    print("=" * 60)
    print(f"           📋 РЕЗУЛЬТАТ: {operation_name}")
    print("=" * 60)

    print("📊 ИСХОДНАЯ таблица:")
    original_table.print_table()

    print("\n🎯 РЕЗУЛЬТАТ операции:")
    result_table.print_table()

    print("\n" + "=" * 60)
    print("Выберите действие:")
    print(" 1. 🔄 ЗАМЕНИТЬ исходную таблицу результатом")
    print(" 2. 💾 Сохранить результат в файл")
    print(" 3. 📝 Продолжить работу с исходной таблицей")
    print(" 0. ↩️  Вернуться (сохранить результат временно)")
    print("=" * 60)

    return get_user_choice(0, 3)


def save_result_menu(result_table):
    """Меню сохранения результата"""
    print("\n💾 Сохранить результат в:")
    print(" 1. CSV файл")
    print(" 2. Pickle файл")
    print(" 3. Текстовый файл")
    print(" 0. Отмена")

    choice = get_user_choice(0, 3)

    if choice == 1:
        filename = input("Введите имя CSV файла: ").strip()
        if filename:
            save_csv(result_table, filename)
            print(f"✅ Результат сохранен в {filename}")
    elif choice == 2:
        filename = input("Введите имя Pickle файла: ").strip()
        if filename:
            save_pickle(result_table, filename)
            print(f"✅ Результат сохранен в {filename}")
    elif choice == 3:
        filename = input("Введите имя текстового файла: ").strip()
        if filename:
            save_text(result_table, filename)
            print(f"✅ Результат сохранен в {filename}")

    input("\nНажмите Enter чтобы продолжить...")


def get_user_choice(min_val, max_val, prompt="Введите номер: "):
    """Утилита для получения выбора пользователя"""
    while True:
        try:
            choice = int(input(prompt))
            if min_val <= choice <= max_val:
                return choice
            else:
                print(f"Пожалуйста, введите число от {min_val} до {max_val}")
        except ValueError:
            print("Пожалуйста, введите корректное число")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')