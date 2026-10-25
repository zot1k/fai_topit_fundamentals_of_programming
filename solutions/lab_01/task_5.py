"""Информационная карточка вычислительного эксперимента.

Программа запрашивает данные об исследователе и параметрах эксперимента,
выполняет базовые вычисления без использования циклов и условий,
а также выводит итоговую карточку и диагностическую информацию о типах данных.
"""

# Входные данные
researcher_name = input("Введите имя исследователя: ")
exp_name = input("Введите название эксперимента: ")
runs_count = int(input("Введите количество выполненных запусков: "))
run_duration = float(input("Введите длительность одного запуска (в секундах): "))
real_part = float(input("Введите действительную часть коэффициента: "))
imag_part = float(input("Введите мнимую часть коэффициента: "))

# Вычисления
total_duration_sec = runs_count * run_duration
total_duration_min = total_duration_sec / 60
coeff = complex(real_part, imag_part)
sq_modulus = real_part ** 2 + imag_part ** 2
has_runs = bool(runs_count)

# Результат (оформление карточки)
print("========================================")
print(f"ЭКСПЕРИМЕНТ: {exp_name}")
print(f"Исследователь: {researcher_name}")
print(f"Запуски: {runs_count}")
print(f"Общее время: {total_duration_sec:.2f} с ({total_duration_min:.2f} мин)")
print(f"Коэффициент: {coeff}")
print(f"Квадрат модуля: {sq_modulus:.2f}")
print(f"Есть выполненные запуски: {has_runs}")
print("========================================")

# Диагностическая строка с типами шести введенных и преобразованных значений
print(f"Типы данных параметров: имя={type(researcher_name).__name__}, "
      f"эксперимент={type(exp_name).__name__}, "
      f"запуски={type(runs_count).__name__}, "
      f"длительность={type(run_duration).__name__}, "
      f"re={type(real_part).__name__}, "
      f"im={type(imag_part).__name__}")
