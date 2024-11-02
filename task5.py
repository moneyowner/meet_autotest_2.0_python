# Напишите код, который запрашивает число и сообщает, является ли оно простым или составным.
# Используйте правило для проверки:
# “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч

num = int(input())
while num < 0 or num > 100000:
    print("Число должно быть положительным и меньше 100000")
    num = float(input())
for i in range(2, num):
    if num % i == 0:
        print("Число является составным")
        break
else:
    print("Число является простым")