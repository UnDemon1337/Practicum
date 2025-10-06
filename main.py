import os
from task1.games import *
from task2.string_calculator import play as play_calculator


def clear_screen():
    """Очищает экран консоли"""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_main_menu():
    """Отображает главное меню выбора задачи"""
    print("=" * 60)
    print("           🎮 КОЛЛЕКЦИЯ ЛОГИЧЕСКИХ ЗАДАЧ")
    print("=" * 60)
    print("Выберите задачу для запуска:")
    print(" 1. Логические игры")
    print(" 2. Строковый калькулятор")
    print(" 0. Выход")
    print("=" * 60)


def display_games_menu():
    """Отображает меню игр"""
    print("=" * 60)
    print("           🎮 ЛОГИЧЕСКИЕ ИГРЫ")
    print("=" * 60)
    print("Выберите игру для запуска:")
    print(" 1. Быки и коровы")
    print(" 2. Крестики-нолики")
    print(" 3. Клондике")
    print(" 0. Назад в главное меню")
    print("=" * 60)


def get_user_choice(min_val, max_val, prompt="Введите номер: "):
    """Получает выбор пользователя"""
    while True:
        try:
            choice = int(input(prompt))
            if min_val <= choice <= max_val:
                return choice
            else:
                print(f"Пожалуйста, введите число от {min_val} до {max_val}")
        except ValueError:
            print("Пожалуйста, введите корректное число")


def run_game(choice):
    """Запускает выбранную игру"""
    games = {
        1: lambda: game1_bulls_and_cows.play(),  # Вызываем метод play() у объекта
        2: lambda: game2_tic_tac_toe.play(),  # Вызываем метод play() у объекта
        3: lambda: game6_klondike.play(),
    }

    if choice in games:
        clear_screen()
        print(f"Запуск игры #{choice}...")
        games[choice]()
        input("\nНажмите Enter чтобы вернуться в меню...")
    else:
        print("Возвращаемся в меню...")


def run_calculator():
    """Запускает строковый калькулятор"""
    clear_screen()
    play_calculator()


def games_section():
    """Раздел с играми"""
    while True:
        clear_screen()
        display_games_menu()
        choice = get_user_choice(0, 3, "Введите номер игры (0-2): ")

        if choice == 0:
            break

        run_game(choice)


def main():
    """Основная функция главного меню"""
    while True:
        clear_screen()
        display_main_menu()
        choice = get_user_choice(0, 2, "Введите номер задачи (0-2): ")

        if choice == 0:
            print("Спасибо за использование! До свидания!")
            break
        elif choice == 1:
            games_section()
        elif choice == 2:
            run_calculator()


if __name__ == "__main__":
    main()