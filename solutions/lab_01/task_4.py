"""Лабораторная работа №1. Задание 4: Строки, Unicode и форматирование."""

# Исходные данные
student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10

# 1. Первый и последний символ имени "Анна"
first_name = student[:4]
last_name = student[5:]
print("Первый символ имени:", first_name[0])
print("Последний символ имени:", first_name[-1])

# 2. Срезы
print("Срез с именем:", first_name)
print("Срез с фамилией:", last_name)

# 3. Верхний и нижний регистры
print("Верхний регистр:", student.upper())
print("Нижний регистр:", student.lower())

# 4. Инициалы А.С.
initials = student[0] + "." + last_name[0] + "."
print("Инициалы:", initials)

# 5. Название курса в обратном порядке
print("Курс в обратном порядке:", course[::-1])

# 6. Форматирование строки тремя способами
percent = (completed / total) * 100

res_percent = "%s — %s: %d/%d (%.1f%%)" % (student, course, completed, total, percent)
res_format = "{0} — {1}: {2}/{3} ({4:.1f}%)".format(student, course, completed, total, percent)
res_fstring = f"{student} — {course}: {completed}/{total} ({percent:.1f}%)"

print("Результат (%):", res_percent)
print("Результат (.format):", res_format)
print("Результат (f-string):", res_fstring)

# 7. Исследование Unicode
symbol = "Я"
code_point = ord(symbol)
restored_symbol = chr(code_point)
utf8_bytes = symbol.encode("utf-8")
utf8_len = len(utf8_bytes)

print("Символ:", symbol)
print("Кодовая позиция (ord):", code_point)
print("Восстановленный символ (chr):", restored_symbol)
print("UTF-8 байты:", utf8_bytes)
print("Длина байтов UTF-8:", utf8_len)

# 8. Попытка изменения первого символа строки по индексу
# Неработающая строка оставлена в файле как комментарий:
# student[0] = "О"  # TypeError: 'str' object does not support item assignment
