import copy


def experiment_a():
    print("=== Эксперимент A. Неизменяемый объект (int) ===")
    a = 10
    b = a

    print(f"До a += 1: a = {a}, b = {b}")
    print(f"id(a) = {id(a)}, id(b) = {id(b)}")

    a += 1

    print(f"После a += 1: a = {a}, b = {b}")
    print(f"id(a) = {id(a)}, id(b) = {id(b)}")
    print(
        "Вывод: Целые числа - неизменяемые объекты (immutable). Операция a += 1 создает новый объект 11 и привязывает к нему имя 'a', имя 'b' продолжает ссылаться на объект 10.\n"
    )


def experiment_b():
    print("=== Эксперимент B. Изменяемый объект (list) ===")
    first = [10, 20]
    second = first

    print(f"До append: first = {first}, second = {second}")
    print(f"id(first) = {id(first)}, id(second) = {id(second)}")

    second.append(30)

    print(f"После second.append(30): first = {first}, second = {second}")
    print(f"id(first) = {id(first)}, id(second) = {id(second)}")

    print("\n--- Дополнительные действия с second ---")
    # 1. Переназначение second на новый список с теми же элементами
    second = [10, 20, 30]

    # 2. Сравнение списков через == и is
    print(f"После переназначения second = [10, 20, 30]:")
    print(f"first == second: {first == second} (равенство значений)")
    print(f"first is second: {first is second} (идентичность объектов)")
    print(f"id(first) = {id(first)}, id(second) = {id(second)}")

    # 3. Изменение нового списка и проверка влияния на first
    second.append(40)
    print(f"\nПосле second.append(40):")
    print(f"first: {first}")
    print(f"second: {second}")
    print(f"Повлияло ли изменение second на first? {'Да' if 40 in first else 'Нет'}\n")


def practical_task():
    print("=== Практическая задача: Конфигурации учебного проекта ===")
    config1 = {
        "name": "Project Alpha",
        "participants": ["Alice", "Bob"],
        "launch_params": ["--debug", ["--port", 8080]],
    }

    # 1. Простое присваивание (ошибочный вариант)
    print("1. Создание config_bad через простое присваивание (config_bad = config1):")
    config_bad = config1
    print(f"До изменения: config1['name'] = {config1['name']}, config_bad['name'] = {config_bad['name']}")

    config_bad["name"] = "Project Shared Bug"
    config_bad["participants"].append("Charlie")

    print(f"После изменения config_bad:")
    print(f"  config1['name']: {config1['name']}")
    print(f"  config1['participants']: {config1['participants']}")
    print(f"  config_bad['participants']: {config_bad['participants']}")
    print(f"  ИТОГ: Изменение config_bad повлияло на config1 (объекты общие: config1 is config_bad => {config1 is config_bad})")

    # Восстановление начального состояния config1
    config1 = {
        "name": "Project Alpha",
        "participants": ["Alice", "Bob"],
        "launch_params": ["--debug", ["--port", 8080]],
    }

    # 2. Создание действительно независимой конфигурации через deepcopy
    print("\n2. Создание config_good через copy.deepcopy(config1):")
    config_good = copy.deepcopy(config1)

    print(f"До изменения: config1['name'] = {config1['name']}, config_good['name'] = {config_good['name']}")

    config_good["name"] = "Project Beta Independent"
    config_good["participants"].append("David")
    config_good["launch_params"][1].append("--ssl")

    print(f"После изменения config_good:")
    print(f"  config1: {config1}")
    print(f"  config_good: {config_good}")

    # Проверка независимости с помощью assert
    assert config1 is not config_good, "Конфигурации должны быть разными объектами"
    assert config1["participants"] is not config_good["participants"], "Списки участников должны быть независимы"
    assert config1["launch_params"] is not config_good["launch_params"], "Параметры запуска должны быть независимы"
    assert config1["launch_params"][1] is not config_good["launch_params"][1], "Вложенные параметры должны быть независимы"
    assert "David" not in config1["participants"], "Изменение config_good не должно изменять config1"

    print("\nИтог проверки с assert: Успешно! Конфигурации полностью независимы.")
    print("  Общие объекты при присваивании: Все (словарная структура, вложенные списки).")
    print("  Независимые объекты при deepcopy: Все уровни вложенных изменяемых структур.")


if __name__ == "__main__":
    experiment_a()
    experiment_b()
    practical_task()
