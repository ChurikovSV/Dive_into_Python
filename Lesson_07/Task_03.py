# Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

from typing import TextIO


def read_or_begin(fd: TextIO) -> str:
    text = fd.readline()
    if not text:
        fd.seek(0)
    return fd.readline().strip()


def converte(numbers: str, names: str, result: str) -> None:
    with (
        open(numbers, "r", encoding="utf-8") as f_numbers,
        open(names, "r", encoding="utf-8") as f_names,
        open(result, "w", encoding="utf-8") as f_result,
    ):

        len_names = sum(1 for _ in f_names)
        len_numbers = sum(1 for _ in f_numbers)

        for _ in range(max(len_names, len_numbers)):
            nums_str = read_or_begin(f_numbers)
            name_str = read_or_begin(f_names)
            print(nums_str)
            num_i, num_f = nums_str.split('|')
            mult = int(num_i) * float(num_f)
            if mult < 0:
                f_result.write(f'{name_str.lower()}{-mult}')
            else:
                f_result.write(f'{name_str.upper()}{int(mult)}')


converte('random_file.txt', 'name.txt', 'result.txt')
