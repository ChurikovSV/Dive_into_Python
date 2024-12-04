# Задание №7
# 📌 Создайте модуль и напишите в нём функцию, которая
# получает на вход дату в формате DD.MM.YYYY
# 📌 Функция возвращает истину, если дата может существовать
# или ложь, если такая дата невозможна.
# 📌 Для простоты договоримся, что год может быть в диапазоне
# [1, 9999].
# 📌 Весь период (1 января 1 года - 31 декабря 9999 года)
# действует Григорианский календарь.
# 📌 Проверку года на високосность вынести в отдельную
# защищённую функцию

def _is_leap(year: int) -> int:
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def is_valid_year(year: str) -> bool:
    day, month, year = map(int, year.split('.'))
    if year < 1 or year > 9999 or month < 1 or month > 12 or day < 1 or day > 31:
        return False
    elif month in (4, 6, 9, 11):
        return day < 31
    elif month == 2:
        if _is_leap(year):
            return day < 30
        else:
            return day < 29
    else:
        return True

date_to_prov = '01.01.2100'
print(is_valid_year(date_to_prov))




