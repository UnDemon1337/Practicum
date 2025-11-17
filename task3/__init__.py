"""
Пакет для работы с табличными данными

Модули:
- table_operations: основные операции с таблицами
- csv_loader: загрузка и сохранение CSV
- pickle_loader: загрузка и сохранение Pickle
- text_saver: сохранение в текстовый файл
- table_manager: интерфейс управления таблицами
- exceptions: пользовательские исключения
"""

from .table_operations import Table
from .csv_loader import load_table as load_csv, save_table as save_csv
from .pickle_loader import load_table as load_pickle, save_table as save_pickle
from .text_saver import save_table as save_text
from .table_manager import play

__all__ = [
    'Table',
    'load_csv',
    'save_csv',
    'load_pickle',
    'save_pickle',
    'save_text',
    'play'
]