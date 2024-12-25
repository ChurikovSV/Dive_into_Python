# Задание №1
# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

import random
import pathlib

MIN_LIMIT = -1000
MAX_LIMIT = 1000


def write_random_to_file(num_pairs: int, file_name: str) -> None:
    with open(file_name, 'a', encoding='UTF-8') as f:
        for _ in range(num_pairs):
            int_num = random.randint(-1000, 1000)
            float_num = random.randint(-1000, 1000)
            f.write(str(int_num) + ' | ' + str(float_num) + '\n')


write_random_to_file(10, 'text/random_file.txt')
