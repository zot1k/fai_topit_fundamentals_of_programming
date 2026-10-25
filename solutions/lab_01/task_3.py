"""Лабораторная работа №1. Задание 3: Числовые типы, операции и преобразования."""

import math

# Эксперимент A. int и арифметические операторы
print("--- Эксперимент A ---")
x = 17
y = 5

print("x + y:", x + y, type(x + y))
print("x - y:", x - y, type(x - y))
print("x * y:", x * y, type(x * y))
print("x / y:", x / y, type(x / y))
print("x // y:", x // y, type(x // y))
print("x % y:", x % y, type(x % y))
print("x ** y:", x ** y, type(x ** y))

# Эксперимент B. Большие целые числа
print("\n--- Эксперимент B ---")
big_num = 2 ** 1000
print("2 ** 1000 =", big_num)
print("Тип 2 ** 1000:", type(big_num))

# Эксперимент C. float
print("\n--- Эксперимент C ---")
result = 0.1 + 0.2
print("0.1 + 0.2 =", result)
print("result == 0.3:", result == 0.3)
print("result - 0.3 =", result - 0.3)
print("math.isclose(result, 0.3):", math.isclose(result, 0.3))

# Эксперимент D. bool, complex и явное преобразование типов
print("\n--- Эксперимент D ---")
v1 = int("42")
v2 = float("3.14")
v3 = str(2026)
v4 = bool(0)
v5 = bool(-1)
v6 = bool("")
v7 = bool("False")
v8 = complex(2, -3)

print("int('42'):", v1, type(v1))
print("float('3.14'):", v2, type(v2))
print("str(2026):", v3, type(v3))
print("bool(0):", v4, type(v4))
print("bool(-1):", v5, type(v5))
print("bool(''):", v6, type(v6))
print("bool('False'):", v7, type(v7))
print("complex(2, -3):", v8, type(v8))
print("Комплексное число - действительная часть:", v8.real, "мнимая часть:", v8.imag)
