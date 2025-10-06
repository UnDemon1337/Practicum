__all__ = [
    'game1_bulls_and_cows',
    'game2_tic_tac_toe',
    'game6_klondike',
]

# Для игр, которые еще не реализованы, создаем заглушки
def play_stub():
    print("Эта игра еще в разработке...")
    input("Нажмите Enter чтобы вернуться в меню...")

from .game1_bulls_and_cows import BullsAndCowsGame
from .game2_tic_tac_toe import TicTacToeGame
from .game6_klondike import KlondikeGame

# Создаем объекты игр
game1_bulls_and_cows = BullsAndCowsGame()
game2_tic_tac_toe = TicTacToeGame()
game6_klondike = KlondikeGame()