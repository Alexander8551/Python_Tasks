import re

def process_command(command, array):
    # Проверка команды на соответствие формату и извлечение параметров
    index_match = re.match(r"Получить элемент по (\d+) индексу", command)
    slice_match = re.match(r"Получить элементы с (\d+) по (\d+) с шагом (\d+)", command)
    reverse_index_match = re.match(r"Получить (\d+)-ый элемент с конца массива", command)

    if index_match:
        # Извлечение индекса
        index = int(index_match.group(1))
        # Проверка границ массива
        if 0 <= index < len(array):
            return array[index]
        else:
            return "Ошибка: Индекс выходит за пределы массива"

    elif slice_match:
        # Извлечение начального, конечного индексов и шага
        start = int(slice_match.group(1))
        end = int(slice_match.group(2))
        step = int(slice_match.group(3))
        # Проверка границ массива
        if 0 <= start < len(array) and 0 <= end <= len(array):
            return array[start:end:step]
        else:
            return "Ошибка: Начальный или конечный индекс выходит за пределы массива"

    elif reverse_index_match:
        # Извлечение индекса с конца
        reverse_index = int(reverse_index_match.group(1))
        # Проверка границ массива
        if 0 < reverse_index <= len(array):
            return array[-reverse_index]
        else:
            return "Ошибка: Индекс с конца выходит за пределы массива"

    else:
        return "Ошибка: Команда не соответствует ожидаемому формату"

# Примеры использования
someArray = [10, 20, 30, 40, 50, 60, 70]
print(process_command("Получить элемент по 2 индексу", someArray))  # Вывод: 30
print(process_command("Получить элементы с 1 по 5 с шагом 2", someArray))  # Вывод: [20, 40]
print(process_command("Получить 2-ый элемент с конца массива", someArray))  # Вывод: 60
print(process_command("Получить элемент по 10 индексу", someArray))  # Вывод: Ошибка: Индекс выходит за пределы массива