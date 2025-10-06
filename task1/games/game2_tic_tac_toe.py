from task1.utils.input_validation import get_valid_coordinates


class TicTacToeGame:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None

    def display_board(self):
        """Отображает игровое поле с красивым форматированием"""
        print("\n   1   2   3")
        print(" ┌───┬───┬───┐")
        for i in range(3):
            row_display = f"{i + 1}│"
            for j in range(3):
                row_display += f" {self.board[i][j]} │"
            print(row_display)
            if i < 2:
                print(" ├───┼───┼───┤")
        print(" └───┴───┴───┘")

    def is_valid_move(self, row, col):
        """Проверяет, допустим ли ход"""
        return self.board[row][col] == ' '

    def check_winner(self):
        """Проверяет, есть ли победитель"""
        # Проверка строк
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != ' ':
                return self.board[row][0]

        # Проверка столбцов
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]

        # Проверка диагоналей
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        return None

    def is_board_full(self):
        """Проверяет, заполнено ли поле"""
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def make_move(self, row, col):
        """Выполняет ход"""
        self.board[row][col] = self.current_player

        # Проверяем победителя
        winner = self.check_winner()
        if winner:
            self.game_over = True
            self.winner = winner
        elif self.is_board_full():
            self.game_over = True

        # Меняем игрока
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def get_player_name(self, symbol):
        """Возвращает имя игрока по символу"""
        return "Игрок 1 (X)" if symbol == 'X' else "Игрок 2 (O)"

    def play_round(self):
        """Один раунд игры"""
        print(f"\nХод: {self.get_player_name(self.current_player)}")
        row, col = get_valid_coordinates("Введите координаты (строка столбец): ", 3, 3)

        if not self.is_valid_move(row, col):
            print("❌ Эта клетка уже занята! Выберите другую.")
            return False

        self.make_move(row, col)
        return True

    def play(self):
        """Основной игровой процесс"""
        print("=" * 50)
        print("           ИГРА: КРЕСТИКИ-НОЛИКИ")
        print("=" * 50)
        print("Правила:")
        print("- Игрок 1: X, Игрок 2: O")
        print("- Игроки по очереди ставят свои символы на поле 3x3")
        print("- Выигрывает тот, кто первым соберет линию из 3 своих символов")
        print("- Линия может быть горизонтальной, вертикальной или диагональной")
        print("- Координаты: строка (1-3) и столбец (1-3), например: '1 2'")
        print("=" * 50)

        input("Нажмите Enter чтобы начать игру...")

        while not self.game_over:
            self.display_board()
            if self.play_round():
                continue

        self.display_board()
        print("\n" + "=" * 30)

        if self.winner:
            winner_name = self.get_player_name(self.winner)
            print(f"🎉 ПОБЕДА! {winner_name} выиграл!")
        else:
            print("🤝 НИЧЬЯ! Поле полностью заполнено!")

        print("=" * 30)


def play():
    """Функция для запуска игры из главного меню"""
    while True:
        game = TicTacToeGame()
        game.play()

        # Спросить о повторной игре
        while True:
            choice = input("\nХотите сыграть еще раз? (да/нет): ").strip().lower()
            if choice in ['да', 'д', 'yes', 'y']:
                break
            elif choice in ['нет', 'н', 'no', 'n']:
                print("Возвращаемся в главное меню...")
                return
            else:
                print("Пожалуйста, введите 'да' или 'нет'")