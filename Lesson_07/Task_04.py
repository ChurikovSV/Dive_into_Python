# Задание №4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона

from random import randint, choices
from string import ascii_lowercase, digits, punctuation


def create_files(
        extension: str = 'bin',
        min_name=6,
        max_name=30,
        min_file=256,
        max_file=4096,
        num_files=2
) -> None:
    for _ in range(num_files):
        name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name, max_name)))
        data = bytes(randint(0, 255) for _ in range(randint(min_file, max_file)))
        with open(f'{name}.{extension}', "wb") as file:
            file.write(data)


create_files()
