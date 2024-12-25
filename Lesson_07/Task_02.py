# Задание №2
# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

import random
import pathlib

VOWELS = 'eyuioa'
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'
MIN_LEN = 4
MAX_LEN = 7


def generate_name(count: int, file_name: str) -> None:
    for _ in range(count):
        first_letter = random.choice([-1, 1])
        name = ''
        for _ in range(random.randint(MIN_LEN, MAX_LEN)):
            if first_letter == -1:
                name += random.choice(CONSONANTS)
            else:
                name += random.choice(VOWELS)
            first_letter *= -1
        with open(file_name, 'a', encoding='UTF-8') as f:
            f.write(name.title() + '\n')

generate_name(10, 'text/name.txt')



                                             
