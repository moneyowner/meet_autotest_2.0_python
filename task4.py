# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

number = input("Введите вещественное число: ")
number = number.replace(',', '')
sum_of_digits = sum(int(digit) for digit in number)
print("Сумма цифр числа:", sum_of_digits)
