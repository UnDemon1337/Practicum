class TableError(Exception):
    """Базовое исключение для ошибок таблиц"""
    pass

class LoadError(TableError):
    """Ошибка загрузки таблицы"""
    pass

class SaveError(TableError):
    """Ошибка сохранения таблицы"""
    pass

class ColumnError(TableError):
    """Ошибка работы со столбцами"""
    pass

class RowError(TableError):
    """Ошибка работы со строками"""
    pass

class TypeError(TableError):
    """Ошибка типов данных"""
    pass

class OperationError(TableError):
    """Ошибка арифметической операции"""
    pass

class MergeError(TableError):
    """Ошибка слияния таблиц"""
    pass