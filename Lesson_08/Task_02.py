# Задание №2
# 📌 Дорабатываем задачу 1.
# 📌 Превратите внешнюю функцию в декоратор.
# 📌 Он должен проверять входят ли переданные в функцию-
# угадайку числа в диапазоны [1, 100] и [1, 10].
# 📌 Если не входят, вызывать функцию со случайными числами
# из диапазонов.

def guess_num(num: int, count: int):

    def guess_game():
        for i in range(1, count + 1):
            print(f'Попытка {i}')
            user_input = int(input('Введите число: '))
            if num == user_input:
                print(f'Вы угадали с {i} попытки.')
                return
            elif num < user_input:
                print('Ваше число больше')
            elif num > user_input:
                print('Ваше число меньше')
    return guess_game



if __name__ == '__main__':
    game = guess_num(num=10, count=10)
    print(game())