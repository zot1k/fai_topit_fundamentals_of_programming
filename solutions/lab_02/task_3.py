import sys
import weakref


def refcount_experiment():
    print("=== Эксперимент 1. Подсчет ссылок (sys.getrefcount) ===")

    data = [1, 2, 3]
    print(
        f"После создания 'data = [1, 2, 3]':                   {sys.getrefcount(data)}"
    )

    alias = data
    print(
        f"После создания 'alias = data':                      {sys.getrefcount(data)}"
    )

    container = [data]
    print(
        f"После помещения в 'container = [data]':             {sys.getrefcount(data)}"
    )

    del alias
    print(
        f"После 'del alias':                                  {sys.getrefcount(data)}"
    )

    container.clear()
    print(
        f"После 'container.clear()':                           {sys.getrefcount(data)}\n"
    )


class Record:
    def __init__(self, name="Default"):
        self.name = name

    def __repr__(self):
        return f"Record({self.name})"


def weakref_experiment():
    print("=== Эксперимент 2. Слабая ссылка (weakref.ref) ===")

    record = Record("TestRecord")
    weak_record = weakref.ref(record)

    print(f"Слабая ссылка до del record: {weak_record()}")
    del record
    print(f"Слабая ссылка после del record: {weak_record()}\n")


def registry_practical_task():
    print("=== Практическая задача: Реестр объектов на WeakValueDictionary ===")

    registry = weakref.WeakValueDictionary()

    # 1. Создаем 3 объекта Record
    r1 = Record("Service1")
    r2 = Record("Service2")

    # Для третьего объекта сохраняем ссылку только во время регистрации
    registry["r1"] = r1
    registry["r2"] = r2
    registry["r3"] = Record("TempService3")

    print(
        f"Реестр после регистрации (для r3 нет сильной переменной): {dict(registry)}"
    )
    print(f"Существующие ключи: {list(registry.keys())}")
    assert "r3" not in registry, "r3 должен был сразу удалиться, так как нет сильной ссылки"

    # 2. Удаляем сильную ссылку r2
    print("\nУдаляем сильную ссылку 'del r2'...")
    del r2
    print(f"Реестр после del r2: {dict(registry)}")
    print(f"Существующие ключи: {list(registry.keys())}")
    assert "r2" not in registry, "r2 должен удалиться из реестра после del r2"
    assert "r1" in registry, "r1 должен остаться в реестре"

    # 3. Удаляем последнюю сильную ссылку r1
    print("\nУдаляем сильную ссылку 'del r1'...")
    del r1
    print(f"Реестр после del r1: {dict(registry)}")
    print(f"Существующие ключи: {list(registry.keys())}")
    assert len(registry) == 0, "Реестр должен стать пустым"

    print(
        "\nВывод: WeakValueDictionary не удерживает объекты в памяти. Как только удаляется последняя сильная ссылка, объект уничтожается и автоматически удаляется из слабой коллекции."
    )


if __name__ == "__main__":
    refcount_experiment()
    weakref_experiment()
    registry_practical_task()
