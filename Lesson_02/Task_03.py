# Задача 3. Перевод целого числа в римское число Программа принимает целое число и возвращает его римское представление в
# виде строки.

# Вводим целое число
num = int(input("Введите целое число: "))
# Массив значений чисел в десятичной системе
val = [
1000, 900, 500, 400,
100, 90, 50, 40,
10, 9, 5, 4,
1
]
# Массив соответствующих римских символов
syb = [
"M", "CM", "D", "CD",
"C", "XC", "L", "XL",
"X", "IX", "V", "IV",
"I"
]
# Инициализируем пустую строку для результата
roman_num = ''
# Индекс для итерации по массивам
i = 0
# Пока значение num больше 0
while num > 0:
# Выполняем цикл для текущего значения в массиве val
    for _ in range(num // val[i]): # num // val[i] дает количество раз, которое val[i] помещается в num
        roman_num += syb[i] # Добавляем соответствующий римскийсимвол в результат
        num -= val[i] # Уменьшаем значение num на val[i]
    i += 1 # Переходим к следующему значению в массиве
# Печатаем результат
print("Результат:", roman_num)