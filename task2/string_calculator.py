class StringCalculator:
    def __init__(self):
        self.number_words = {
            # Основные числа
            'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5,
            'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9, 'десять': 10,
            'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13, 'четырнадцать': 14,
            'пятнадцать': 15, 'шестнадцать': 16, 'семнадцать': 17, 'восемнадцать': 18,
            'девятнадцать': 19, 'двадцать': 20, 'тридцать': 30, 'сорок': 40,
            'пятьдесят': 50, 'шестьдесят': 60, 'семьдесят': 70, 'восемьдесят': 80,
            'девяносто': 90,
            # Особые формы для дробей
            'одна': 1, 'две': 2
        }

        self.reverse_number_words = {
            0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
            6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять',
            11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать',
            15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать',
            19: 'девятнадцать', 20: 'двадцать', 30: 'тридцать', 40: 'сорок',
            50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят', 80: 'восемьдесят',
            90: 'девяносто'
        }

        self.fraction_words = {
            'половина': (1, 2), 'треть': (1, 3), 'четверть': (1, 4),
            'пятая': (1, 5), 'шестая': (1, 6), 'седьмая': (1, 7),
            'восьмая': (1, 8), 'девятая': (1, 9), 'десятая': (1, 10),
            'одиннадцатая': (1, 11), 'двенадцатая': (1, 12),
            'третьих': (1, 3), 'четвертых': (1, 4), 'пятых': (1, 5),
            'шестых': (1, 6), 'седьмых': (1, 7), 'восьмых': (1, 8),
            'девятых': (1, 9), 'десятых': (1, 10),
            'вторая': (1, 2), 'вторых': (1, 2)
        }

        self.operations = {
            'плюс': '+',
            'минус': '-',
            'умножить': '*'
        }

    def words_to_number(self, words):
        """Преобразует слова в число"""
        if not words:
            return 0

        # Проверяем, является ли это дробью
        if len(words) == 1 and words[0] in self.fraction_words:
            return self.fraction_words[words[0]]

        # Проверяем смешанную дробь
        if 'и' in words:
            idx = words.index('и')
            whole_part = self.words_to_integer(words[:idx])
            fraction_part = self.words_to_fraction(words[idx + 1:])
            return (whole_part * fraction_part[1] + fraction_part[0], fraction_part[1])

        # Проверяем обычную дробь (формат "числитель знаменатель")
        if len(words) == 2:
            # Проверяем, является ли второе слово дробью
            if words[1] in self.fraction_words or any(words[1].endswith(ending) for ending in ['ых', 'их', 'ая']):
                return self.words_to_fraction(words)

        # Целое число
        return self.words_to_integer(words)

    def words_to_integer(self, words):
        """Преобразует слова в целое число"""
        result = 0
        temp = 0

        for word in words:
            if word in self.number_words:
                value = self.number_words[word]
                if value >= 20:
                    temp += value
                else:
                    if temp == 0:
                        result += value
                    else:
                        result += temp + value
                        temp = 0
            elif word != 'и':
                # Попробуем найти основу слова для дробей
                base_word = self.get_base_fraction_word(word)
                if base_word:
                    value = self.number_words.get(base_word)
                    if value is not None:
                        if temp == 0:
                            result += value
                        else:
                            result += temp + value
                            temp = 0
                    else:
                        raise ValueError(f"Неизвестное число: {word}")
                else:
                    raise ValueError(f"Неизвестное число: {word}")

        return result + temp

    def get_base_fraction_word(self, word):
        """Возвращает основу слова для дробей"""
        if word == 'одна':
            return 'один'
        elif word == 'две':
            return 'два'
        elif word.endswith('ая') or word.endswith('ых') or word.endswith('их'):
            base = word[:-2]  # Убираем окончание
            if base in self.number_words:
                return base
        return None

    def words_to_fraction(self, words):
        """Преобразует слова в дробь"""
        if len(words) == 1:
            if words[0] in self.fraction_words:
                return self.fraction_words[words[0]]
            else:
                raise ValueError(f"Неизвестная дробь: {words[0]}")

        # Формат "числитель знаменатель" (например: "одна вторая", "четыре пятых")
        if len(words) == 2:
            # Обрабатываем числитель
            numerator_word = words[0]
            if numerator_word == 'одна':
                numerator = 1
            elif numerator_word == 'две':
                numerator = 2
            else:
                numerator = self.words_to_integer([numerator_word])

            # Обрабатываем знаменатель
            denominator_word = words[1]

            if denominator_word in self.fraction_words:
                denominator = self.fraction_words[denominator_word][1]
                return (numerator, denominator)
            else:
                # Пытаемся определить знаменатель по окончанию
                if denominator_word.endswith('ая'):
                    # Например: "вторая", "третья"
                    base = denominator_word[:-2]
                    if base == 'втор':
                        denominator = 2
                    elif base == 'треть':
                        denominator = 3
                    elif base == 'четверт':
                        denominator = 4
                    else:
                        # Для других чисел пытаемся найти основу
                        if base in self.number_words:
                            denominator = self.number_words[base]
                        else:
                            raise ValueError(f"Неизвестный знаменатель: {denominator_word}")
                elif denominator_word.endswith('ых') or denominator_word.endswith('их'):
                    # Например: "пятых", "шестых"
                    base = denominator_word[:-3] if denominator_word.endswith('ых') else denominator_word[:-2]
                    if base in self.number_words:
                        denominator = self.number_words[base]
                    else:
                        # Специальные случаи
                        if base == 'треть':
                            denominator = 3
                        elif base == 'четверт':
                            denominator = 4
                        else:
                            raise ValueError(f"Неизвестный знаменатель: {denominator_word}")
                else:
                    raise ValueError(f"Неизвестный формат дроби: {denominator_word}")

                return (numerator, denominator)

        raise ValueError(f"Некорректный формат дроби: {' '.join(words)}")

    def number_to_words(self, number):
        """Преобразует число в слова"""
        if isinstance(number, tuple):
            # Дробь
            numerator, denominator = number
            if numerator == 0:
                return "ноль"
            elif numerator < denominator:
                # Правильная дробь
                numerator_word = self.integer_to_words(numerator, is_fraction=True)
                denominator_word = self.get_denominator_word(denominator, numerator)
                return f"{numerator_word} {denominator_word}"
            else:
                # Смешанная дробь
                whole = numerator // denominator
                remainder = numerator % denominator
                if remainder == 0:
                    return self.integer_to_words(whole)
                else:
                    whole_word = self.integer_to_words(whole)
                    fraction_word = self.number_to_words((remainder, denominator))
                    return f"{whole_word} и {fraction_word}"
        else:
            # Целое число
            return self.integer_to_words(number)

    def integer_to_words(self, num, is_fraction=False):
        """Преобразует целое число в слова"""
        if num == 0:
            return "ноль"

        if num <= 20:
            word = self.reverse_number_words[num]
            if is_fraction:
                if num == 1:
                    return "одна"
                elif num == 2:
                    return "две"
            return word

        tens = (num // 10) * 10
        units = num % 10

        if units == 0:
            return self.reverse_number_words[tens]
        else:
            tens_word = self.reverse_number_words[tens]
            units_word = self.integer_to_words(units, is_fraction)
            return f"{tens_word} {units_word}"

    def get_denominator_word(self, denominator, numerator):
        """Возвращает правильное слово для знаменателя"""
        if denominator == 2:
            return "вторая" if numerator == 1 else "вторых"
        elif denominator == 3:
            return "треть" if numerator == 1 else "третьих"
        elif denominator == 4:
            return "четверть" if numerator == 1 else "четвертых"
        else:
            base = self.integer_to_words(denominator, is_fraction=True)
            if numerator == 1:
                if base.endswith('ь'):
                    return base[:-1] + 'ая'
                else:
                    return base + 'ая'
            else:
                if base.endswith('ь'):
                    return base[:-1] + 'ых'
                else:
                    return base + 'ых'

    # Остальные методы остаются без изменений...
    def calculate(self, a, b, operation):
        """Выполняет арифметическую операцию"""
        if operation == '+':
            if isinstance(a, tuple) or isinstance(b, tuple):
                return self.add_fractions(
                    a if isinstance(a, tuple) else (a, 1),
                    b if isinstance(b, tuple) else (b, 1)
                )
            return a + b
        elif operation == '-':
            if isinstance(a, tuple) or isinstance(b, tuple):
                return self.subtract_fractions(
                    a if isinstance(a, tuple) else (a, 1),
                    b if isinstance(b, tuple) else (b, 1)
                )
            return a - b
        elif operation == '*':
            if isinstance(a, tuple) or isinstance(b, tuple):
                return self.multiply_fractions(
                    a if isinstance(a, tuple) else (a, 1),
                    b if isinstance(b, tuple) else (b, 1)
                )
            return a * b

    def add_fractions(self, frac1, frac2):
        """Сложение дробей"""
        a_num, a_den = frac1
        b_num, b_den = frac2

        numerator = a_num * b_den + b_num * a_den
        denominator = a_den * b_den

        return self.simplify_fraction((numerator, denominator))

    def subtract_fractions(self, frac1, frac2):
        """Вычитание дробей"""
        a_num, a_den = frac1
        b_num, b_den = frac2

        numerator = a_num * b_den - b_num * a_den
        denominator = a_den * b_den

        if numerator < 0:
            raise ValueError("Результат отрицательный")

        return self.simplify_fraction((numerator, denominator))

    def multiply_fractions(self, frac1, frac2):
        """Умножение дробей"""
        a_num, a_den = frac1
        b_num, b_den = frac2

        numerator = a_num * b_num
        denominator = a_den * b_den

        return self.simplify_fraction((numerator, denominator))

    def simplify_fraction(self, fraction):
        """Упрощает дробь"""
        numerator, denominator = fraction

        if numerator == 0:
            return 0

        # Находим НОД
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        common_divisor = gcd(numerator, denominator)
        numerator //= common_divisor
        denominator //= common_divisor

        return (numerator, denominator)

    def parse_expression(self, expression):
        """Разбирает строковое выражение"""
        words = expression.lower().split()

        # Находим операцию
        operation_idx = -1
        operation = None

        for i, word in enumerate(words):
            if word in self.operations:
                operation_idx = i
                operation = self.operations[word]
                break

        if operation_idx == -1:
            raise ValueError("Операция не найдена")

        # Разделяем на левую и правую части
        left_words = words[:operation_idx]
        right_words = words[operation_idx + 1:]

        if not left_words or not right_words:
            raise ValueError("Неполное выражение")

        # Преобразуем в числа
        left_number = self.words_to_number(left_words)
        right_number = self.words_to_number(right_words)

        return left_number, right_number, operation

    def calc(self, expression):
        """Основная функция калькулятора"""
        try:
            a, b, operation = self.parse_expression(expression)
            result = self.calculate(a, b, operation)
            return self.number_to_words(result)
        except Exception as e:
            return f"Ошибка: {str(e)}"


def play():
    """Функция для запуска калькулятора из меню"""
    calculator = StringCalculator()

    print("=" * 60)
    print("           🧮 СТРОКОВЫЙ КАЛЬКУЛЯТОР")
    print("=" * 60)
    print("Поддерживаемые операции:")
    print("- Целые числа: двадцать пять плюс тринадцать")
    print("- Дроби: одна вторая плюс три четвертых")
    print("- Смешанные дроби: один и четыре пятых плюс шесть седьмых")
    print("=" * 60)

    examples = [
        "двадцать пять плюс тринадцать",
        "сорок пять минус восемнадцать",
        "семь умножить шесть",
        "одна вторая плюс три четвертых",
        "один и четыре пятых плюс шесть седьмых"
    ]

    print("Примеры использования:")
    for i, example in enumerate(examples, 1):
        print(f"{i}. {example}")
    print("=" * 60)

    while True:
        print("\nВведите выражение (или 'выход' для возврата в меню):")
        expression = input("> ").strip()

        if expression.lower() in ['выход', 'exit', 'quit', '0']:
            print("Возвращаемся в меню...")
            break

        if not expression:
            continue

        result = calculator.calc(expression)
        print(f"Результат: {result}")


# Тестирование
if __name__ == "__main__":
    calculator = StringCalculator()
