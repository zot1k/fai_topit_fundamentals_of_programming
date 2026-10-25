"""Лабораторная работа №1. Задание 2: Имена, объекты и сравнение."""

a = 1000
b = a
c = int("1000")

# Прогноз результата четырех сравнений:
# 1. a == b -> True (значения объектов равны: 1000 == 1000)
# 2. a is b -> True (связывание b = a делает b ссылкой на тот же объект, что и a)
# 3. a == c -> True (значения объектов равны: 1000 == 1000)
# 4. a is c -> False (вызов int("1000") создает новый объект int в памяти, поэтому id(a) != id(c))

print("Типы:", type(a), type(b), type(c))
print("Идентификаторы:", id(a), id(b), id(c))
print("a == b:", a == b)
print("a is b:", a is b)
print("a == c:", a == c)
print("a is c:", a is c)

# 3. Измените значение c на None и добавьте корректную проверку
c = None
print("c is None:", c is None)

# 4. Сравнение строк
first = "python"
second = "py" + "thon"

print("first == second:", first == second)
print("first is second:", first is second)
