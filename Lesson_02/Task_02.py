# Задание 2. Преобразование числа в шестнадцатеричное представление
# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление. Функцию hex используйте для
# проверки своего результата

# Примеры чисел
numbers = [255, 16, 0, -42]
# Определяем символы для цифр в шестнадцатеричной системе
hex_digits = '0123456789ABCDEF'
for number in numbers:
    if number == 0:
        hex_string = '0'
    else:
        is_negative = number < 0
        if is_negative:
            number = -number
        hex_string = ''
        while number > 0:
            remainder = number % 16
            hex_string = hex_digits[remainder] + hex_string
            number //= 16
        if is_negative:
            hex_string = '-' + hex_string
    print(hex_string)