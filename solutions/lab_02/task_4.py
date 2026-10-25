import gc
import sys


def basic_cycle_experiment():
    print("=== Эксперимент 1. Простая циклическая ссылка и GC ===")

    first = []
    second = []
    first.append(second)
    second.append(first)

    print(f"first ссылается на second: {first[0] is second}")
    print(f"second ссылается на first: {second[0] is first}")

    print(f"Состояние GC (включен): {gc.isenabled()}")
    print(f"Пороги поколений (thresholds): {gc.get_threshold()}")
    print(f"Счетчики поколений (counts): {gc.get_count()}")

    first_id = id(first)
    second_id = id(second)
    print(f"Сохраненные ID: first_id={first_id}, second_id={second_id}")

    del first
    del second

    collected = gc.collect()
    print(f"Количество объектов, собранных gc.collect(): {collected}\n")


def disabled_gc_experiment():
    print("=== Эксперимент 2. Отключение и ручной запуск сборщика мусора ===")

    gc.disable()
    print(f"Статус GC после gc.disable(): {gc.isenabled()}")

    # Создание нескольких циклических структур
    cycles = []
    for i in range(5):
        a = {}
        b = {}
        a["next"] = b
        b["prev"] = a
        cycles.append((a, b))

    del cycles  # удаляем внешнюю ссылку на кортежи циклов

    print("Циклические структуры созданы и внешние ссылки удалены (GC выключен).")

    # Ручная сборка
    collected = gc.collect()
    print(f"Собрано объектов ручным вызовом gc.collect(): {collected}")

    gc.enable()
    print(f"Статус GC после gc.enable(): {gc.isenabled()}\n")


def graph_practical_task():
    print("=== Практическая задача: Модель графа (цикл из 3 узлов + 1 независимый) ===")

    # Предварительная очистка для чистоты эксперимента
    gc.collect()

    # 4 независимый узел
    node4 = {"name": "Node4_Independent", "data": 42, "neighbors": []}

    # 3 циклических узла
    node1 = {"name": "Node1", "neighbors": []}
    node2 = {"name": "Node2", "neighbors": []}
    node3 = {"name": "Node3", "neighbors": []}

    # Замыкаем цикл 1 -> 2 -> 3 -> 1
    node1["neighbors"].append(node2)
    node2["neighbors"].append(node3)
    node3["neighbors"].append(node1)

    print("Связи графа:")
    print(f"  Node1 -> {node1['neighbors'][0]['name']}")
    print(f"  Node2 -> {node2['neighbors'][0]['name']}")
    print(f"  Node3 -> {node3['neighbors'][0]['name']}")
    print(f"  Node4 (Независимый) -> {node4['neighbors']}")

    # Удаляем внешние имена циклических узлов
    print("\nУдаляем внешние имена node1, node2, node3...")
    del node1
    del node2
    del node3

    collected = gc.collect()
    print(f"Объектов собрано циклической сборкой мусора: {collected}")

    # Проверяем доступность и целостность независимого узла node4
    print(f"\nПроверка независимого узла node4:")
    print(f"  node4: {node4}")
    assert node4["name"] == "Node4_Independent", "Независимый узел должен быть неизменен"
    assert node4["data"] == 42, "Данные независимого узла должны быть сохранены"

    print("Итог: Независимый узел полностью доступен, а изолированный цикл 1-2-3 успешно удален сборщиком мусора.")


if __name__ == "__main__":
    basic_cycle_experiment()
    disabled_gc_experiment()
    graph_practical_task()
