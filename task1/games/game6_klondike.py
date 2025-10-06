from task1.utils.input_validation import get_valid_input  # Измененный импорт


class KlondikeGame:
    def __init__(self):
        self.board_size = 10
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 1
        self.game_over = False
        self.winner = None

    def print_board(self):
        """Отображает игровое поле"""
        print("\n" + "=" * 50)
        print("           ИГРА: КЛОНДАЙК")
        print("=" * 50)
        print("   " + " ".join(str(i) for i in range(self.board_size)))

        for i in range(self.board_size):
            row_display = [str(i)]
            for j in range(self.board_size):
                if self.board[i][j] == 'X':
                    row_display.append('X')
                elif self.board[i][j] == 'O':
                    row_display.append('O')
                else:
                    row_display.append('.')
            print(" " + " ".join(row_display))

        print("=" * 50)
        print(f"Игрок 1: X | Игрок 2: O")
        print(f"Сейчас ходит: Игрок {self.current_player}")
        print("=" * 50)

    def is_valid_move(self, move_input):
        """Проверяет корректность ввода координат"""
        try:
            coords = move_input.split()
            if len(coords) != 2:
                return False, "Введите ровно два числа через пробел!"

            row, col = int(coords[0]), int(coords[1])

            if row < 0 or row >= self.board_size or col < 0 or col >= self.board_size:
                return False, f"Координаты должны быть от 0 до {self.board_size - 1}!"

            if self.board[row][col] != ' ':
                return False, "Эта клетка уже занята!"

            return True, ""

        except ValueError:
            return False, "Введите числа корректно!"

    def make_move(self, row, col):
        """Выполняет ход игрока"""
        mark = 'X' if self.current_player == 1 else 'O'
        self.board[row][col] = mark

    def check_chain_length(self, row, col, dx, dy):
        """Проверяет длину цепочки в заданном направлении"""
        mark = self.board[row][col]
        length = 1

        # Проверяем в прямом направлении
        r, c = row + dx, col + dy
        while 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[r][c] != ' ':
            length += 1
            r += dx
            c += dy

        # Проверяем в обратном направлении
        r, c = row - dx, col - dy
        while 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[r][c] != ' ':
            length += 1
            r -= dx
            c -= dy

        return length

    def check_loss_condition(self, row, col):
        """Проверяет, создал ли ход проигрышную цепочку"""
        # Все 8 направлений: горизонталь, вертикаль, две диагонали
        directions = [
            (0, 1),  # горизонталь вправо
            (1, 0),  # вертикаль вниз
            (1, 1),  # диагональ вправо-вниз
            (1, -1),  # диагональ влево-вниз
            (0, -1),  # горизонталь влево
            (-1, 0),  # вертикаль вверх
            (-1, -1),  # диагональ влево-вверх
            (-1, 1)  # диагональ вправо-вверх
        ]

        for dx, dy in directions:
            chain_length = self.check_chain_length(row, col, dx, dy)
            if chain_length >= 3:
                return True

        return False

    def is_board_full(self):
        """Проверяет, заполнено ли все поле"""
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def switch_player(self):
        """Переключает текущего игрока"""
        self.current_player = 3 - self.current_player  # 1 -> 2, 2 -> 1

    def play_round(self):
        """Один раунд игры"""
        self.print_board()

        move_input = get_valid_input(
            f"Игрок {self.current_player}, введите координаты хода (строка столбец): ",
            validation_func=self.is_valid_move,
            error_message="Некорректный ввод. Попробуйте еще раз."
        )

        row, col = map(int, move_input.split())
        self.make_move(row, col)

        # Проверяем условие проигрыша
        if self.check_loss_condition(row, col):
            self.game_over = True
            self.winner = 3 - self.current_player  # Победитель - противоположный игрок
            self.print_board()
            print(f"\n💥 Игрок {self.current_player} создал цепочку из 3+ фишек!")
            print(f"🎉 ПОБЕДИТЕЛЬ: Игрок {self.winner}!")
        elif self.is_board_full():
            self.game_over = True
            self.print_board()
            print(f"\n🏁 Все клетки заполнены!")
            print("📝 РЕЗУЛЬТАТ: НИЧЬЯ!")
        else:
            self.switch_player()

    def play(self):
        """Основной игровой процесс"""
        print("=" * 50)
        print("           ИГРА: КЛОНДАЙК")
        print("=" * 50)
        print("Правила:")
        print("- Игровое поле: 10x10 клеток")
        print("- Игрок 1 ставит X, Игрок 2 ставит O")
        print("- Игроки ходят по очереди")
        print("- Проигрывает тот, после чьего хода образуется")
        print("  цепочка из 3+ фишек (включая фишки соперника)")
        print("- Цепочка может быть в любом из 8 направлений")
        print("- Координаты вводятся как 'строка столбец' (0-9)")
        print("=" * 50)
        print("Начало игры!")

        while not self.game_over:
            self.play_round()


def play():
    """Функция для запуска игры из главного меню"""
    game = KlondikeGame()
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