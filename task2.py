# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

print("Введите х1")
x1 = int(input())
print("Введите y1")
y1 = int(input())
print("Введите х2")
x2 = int(input())
print("Введите y2")
y2 = int(input())

distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
print("Расстояние =", round(distance, 3))