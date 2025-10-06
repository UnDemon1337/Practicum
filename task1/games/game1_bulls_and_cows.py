import random
from task1.utils.input_validation import get_valid_input


class BullsAndCowsGame:
    def __init__(self):
        self.secret_number = None
        self.attempts = 0
        self.game_over = False

    def generate_secret_number(self):
        """Генерирует 4-значное число с неповторяющимися цифрами"""
        digits = list(range(10))
        random.shuffle(digits)
        while digits[0] == 0:
            random.shuffle(digits)
        self.secret_number = ''.join(map(str, digits[:4]))

    def is_valid_guess(self, guess):
        """Проверяет корректность ввода пользователя"""
        if not guess.isdigit():
            return False, "Введите только цифры!"

        if len(guess) != 4:
            return False, "Число должно быть 4-значным!"

        if guess[0] == '0':
            return False, "Число не может начинаться с 0!"

        if len(set(guess)) != 4:
            return False, "Все цифры должны быть разными!"

        return True, ""

    def calculate_bulls_and_cows(self, guess):
        """Вычисляет количество быков и коров"""
        bulls = 0
        cows = 0

        for i in range(4):
            if guess[i] == self.secret_number[i]:
                bulls += 1
            elif guess[i] in self.secret_number:
                cows += 1

        return bulls, cows

    def play_round(self):
        """Один раунд игры"""
        guess = get_valid_input(
            "Введите ваше 4-значное число: ",
            validation_func=self.is_valid_guess,
            error_message="Некорректный ввод. Попробуйте еще раз."
        )

        self.attempts += 1
        bulls, cows = self.calculate_bulls_and_cows(guess)

        if bulls == 4:
            self.game_over = True
            print(f"\n🎉 ПОЗДРАВЛЯЮ! Вы угадали число {self.secret_number}!")
            print(f"Количество попыток: {self.attempts}")
        else:
            print(f"Быки: {bulls}, Коровы: {cows}")

            # Подсказки
            if bulls == 0 and cows == 0:
                print("❌ Ни одна цифра не подходит")
            elif bulls == 3:
                print("🔥 Очень близко! Осталась одна цифра не на месте")
            elif cows == 4:
                print("🔀 Все цифры есть в числе, но все не на своих местах!")

    def play(self):
        """Основной игровой процесс"""
        print("=" * 50)
        print("           ИГРА 1: БЫКИ И КОРОВЫ")
        print("=" * 50)
        print("Правила:")
        print("- Я загадал 4-значное число с неповторяющимися цифрами")
        print("- Быки: цифра на своем месте")
        print("- Коровы: цифра есть в числе, но не на своем месте")
        print("- Число не может начинаться с 0")
        print("=" * 50)

        self.generate_secret_number()
        print("Число загадано! Попробуйте угадать.")

        while not self.game_over:
            print(f"\nПопытка #{self.attempts + 1}")
            self.play_round()


def play():
    """Функция для запуска игры из главного меню"""
    game = BullsAndCowsGame()
    game.play()

    # Спросить о повторной игре
    while True:
        choice = input("\nХотите сыграть еще раз? (да/нет): ").strip().lower()
        if choice in ['да', 'д', 'yes', 'y']:
            play()  # Рекурсивный вызов для новой игры
            break
        elif choice in ['нет', 'н', 'no', 'n']:
            print("Возвращаемся в главное меню...")
            break
        else:
            print("Пожалуйста, введите 'да' или 'нет'")