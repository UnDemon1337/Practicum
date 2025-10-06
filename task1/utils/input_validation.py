def get_valid_input(prompt, validation_func=None, error_message="Некорректный ввод"):
    """
    Универсальная функция для получения валидного ввода
    """
    while True:
        user_input = input(prompt).strip()

        # Если функция проверки не предоставлена, возвращаем ввод как есть
        if validation_func is None:
            return user_input

        is_valid, message = validation_func(user_input)

        if is_valid:
            return user_input
        else:
            if message:
                print(f"{error_message}: {message}")
            else:
                print(error_message)


def get_valid_coordinates(prompt, max_row, max_col):
    """
    Получает корректные координаты от пользователя (для игр с координатами 1-based)
    """
    while True:
        try:
            coords = input(prompt).strip().split()
            if len(coords) != 2:
                print("Введите две координаты через пробел (например: 1 2)")
                continue

            row = int(coords[0])
            col = int(coords[1])

            if 1 <= row <= max_row and 1 <= col <= max_col:
                return row - 1, col - 1  # Convert to 0-based indexing
            else:
                print(f"Координаты должны быть в диапазоне 1-{max_row} и 1-{max_col}")

        except ValueError:
            print("Пожалуйста, введите числа!")


def get_valid_klondike_coordinates(prompt, board_size=10):
    """
    Специальная функция для игры Клондайк (0-based координаты)
    """
    while True:
        try:
            coords = input(prompt).strip().split()
            if len(coords) != 2:
                print("Введите две координаты через пробел (например: 5 5)")
                continue

            row = int(coords[0])
            col = int(coords[1])

            if 0 <= row < board_size and 0 <= col < board_size:
                return row, col  # 0-based indexing
            else:
                print(f"Координаты должны быть в диапазоне 0-{board_size - 1}")

        except ValueError:
            print("Пожалуйста, введите числа!")