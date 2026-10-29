import sys
import tracemalloc
from memory_report import generate_memory_report, print_memory_report


def part_1_object_sizes():
    print("=== Часть 1. Размеры отдельных объектов (sys.getsizeof) ===")

    objects = [
        ("Пустой список []", []),
        ("Список из 10 целых чисел", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ("Кортеж из 10 целых чисел", (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)),
        ("Строка из 10 символов '0123456789'", "0123456789"),
        ("Целое число 0", 0),
        ("Объект None", None),
    ]

    for label, obj in objects:
        size = sys.getsizeof(obj)
        print(f"  {label:<35}: {size} байт")

    print(
        "\nОбъяснение: Размер контейнера отражает лишь сам заголовок CPython-структуры и массив указателей на элементы, но не включает размер объектов, на которые эти указатели ссылаются."
    )
    print()


def part_2_list_growth():
    print("=== Часть 2. Рост динамического списка ===")
    print("Отслеживание изменений размера при добавлении 100 элементов:")

    lst = []
    prev_size = sys.getsizeof(lst)
    print(f"  Длина: {len(lst):3d} | Размер (байты): {prev_size:4d} (Начальный размер)")

    for i in range(1, 101):
        lst.append(i)
        current_size = sys.getsizeof(lst)
        if current_size != prev_size:
            print(
                f"  Длина: {len(lst):3d} | Размер (байты): {current_size:4d} (Прирост: +{current_size - prev_size} B)"
            )
            prev_size = current_size

    print(
        "\nВывод: CPython резервирует память с запасом (over-allocation) по формуле pattern: 0, 4, 8, 16, 25, 35, 46, 58, 72, 88, 106... Это обеспечивает амортизированную сложность O(1) для append().\n"
    )


def part_3_tracemalloc_comparison():
    print("=== Часть 3. Измерение выделения памяти через tracemalloc ===")

    # 1. Сценарий list(range(100_000))
    tracemalloc.start()
    tracemalloc.reset_peak()
    numbers_list = list(range(100_000))
    cur_list, peak_list = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("Сценарий 1: numbers = list(range(100_000))")
    print(f"  Текущая память: {cur_list / 1024:.2f} KB")
    print(f"  Пиковая память:  {peak_list / 1024:.2f} KB")

    # 2. Сценарий range(100_000)
    tracemalloc.start()
    tracemalloc.reset_peak()
    numbers_range = range(100_000)
    cur_range, peak_range = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("\nСценарий 2: numbers = range(100_000)")
    print(f"  Текущая память: {cur_range / 1024:.2f} KB")
    print(f"  Пиковая память:  {peak_range / 1024:.2f} KB")

    print(
        "\nСформулированный вывод: list(range(100_000)) материализует все 100,000 объектов/указателей в памяти (~800 KB), тогда как range(100_000) — это ленивый объект фиксированного размера (start, stop, step), занимающий доли килобайта независимо от N."
    )
    print()


def practical_task_report():
    print("=== Практическая задача. Запуск утилиты memory_report.py ===")
    report_data = generate_memory_report(100_000)
    print_memory_report(report_data)


if __name__ == "__main__":
    part_1_object_sizes()
    part_2_list_growth()
    part_3_tracemalloc_comparison()
    practical_task_report()
