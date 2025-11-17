from task3.exceptions import SaveError


def save_table(table, filename, max_col_width=20):
    """
    Сохранение таблицы в текстовый файл

    Args:
        table: объект Table
        filename: имя файла
        max_col_width: максимальная ширина столбца
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            if not table.headers and not table.data:
                file.write("Таблица пуста\n")
                return

            # Определяем ширину столбцов
            col_widths = []
            for i, header in enumerate(table.headers):
                max_width = len(str(header))
                for row in table.data:
                    if i < len(row):
                        max_width = min(max(max_width, len(str(row[i]))), max_col_width)
                col_widths.append(max_width + 2)

            # Вывод заголовков
            header_line = "|"
            for i, header in enumerate(table.headers):
                header_str = str(header)
                if len(header_str) > max_col_width:
                    header_str = header_str[:max_col_width - 3] + "..."
                header_line += f" {header_str:<{col_widths[i]}} |"
            file.write(header_line + "\n")

            # Разделитель
            separator = "+"
            for width in col_widths:
                separator += "-" * (width + 2) + "+"
            file.write(separator + "\n")

            # Вывод данных
            for row in table.data:
                row_line = "|"
                for i in range(len(table.headers)):
                    if i < len(row):
                        value_str = str(row[i])
                        if len(value_str) > max_col_width:
                            value_str = value_str[:max_col_width - 3] + "..."
                    else:
                        value_str = ""
                    row_line += f" {value_str:<{col_widths[i]}} |"
                file.write(row_line + "\n")

    except Exception as e:
        raise SaveError(f"Ошибка сохранения текстового файла: {str(e)}")