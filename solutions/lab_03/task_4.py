from typing import Callable, Optional


def arithmetic_mean(values: list[float]) -> float:
    """Возвращает среднее арифметическое непустого списка."""
    if not values:
        return 0.0
    total = 0.0
    for v in values:
        total += v
    return total / len(values)


def normalize_name(name: str) -> str:
    """Удаляет лишние пробелы и приводит каждую часть имени к нужному регистру."""
    if not name or not name.strip():
        return ""
    parts = name.strip().split()
    return " ".join(p.capitalize() for p in parts)


def build_report(
    student: str,
    results: list[int],
    *,
    precision: int = 2,
    prefix: str = "Результат",
) -> str:
    """Формирует строковый отчет о результатах студента."""
    clean_name = normalize_name(student)
    if not results:
        return f"{prefix}: {clean_name} — нет оценок"
    total = 0
    for r in results:
        total += r
    avg = total / len(results)
    return f"{prefix}: {clean_name}, средний балл: {avg:.{precision}f}"


def collect_tags(*tags: str, lowercase: bool = True) -> tuple[str, ...]:
    """Возвращает очищенные теги без пустых значений и повторов."""
    unique = []
    seen = set()
    for t in tags:
        clean = t.strip()
        if not clean:
            continue
        val = clean.lower() if lowercase else clean
        if val not in seen:
            seen.add(val)
            unique.append(val)
    return tuple(unique)


course = "Python"


def outer_function():
    topic = "Функции"

    def inner_function():
        nonlocal topic
        topic = "Функции и замыкания"
        return f"Курс: {course}, тема: {topic}"

    res = inner_function()
    return topic, res


def buggy_add_result(value, results=[]):
    results.append(value)
    return results


def fixed_add_result(value, results=None):
    if results is None:
        results = []
    results.append(value)
    return results


def apply_to_results(operation: Callable[[float], float], values: list[float]) -> list[float]:
    return [operation(v) for v in values]


def make_threshold_checker(threshold: float) -> Callable[[float], bool]:
    def check(score: float) -> bool:
        return score >= threshold
    return check


if __name__ == "__main__":
    assert arithmetic_mean([]) == 0.0
    assert arithmetic_mean([10.0]) == 10.0
    assert arithmetic_mean([2.0, 4.0, 6.0]) == 4.0

    assert normalize_name("") == ""
    assert normalize_name("  иван   иванович  ") == "Иван Иванович"
    assert normalize_name("анна") == "Анна"

    assert "нет оценок" in build_report("борис", [])
    assert "85.0" in build_report("анна", [80, 90], precision=1)
    assert "Итог: Иван" in build_report("иван", [100], prefix="Итог")

    assert collect_tags() == ()
    assert collect_tags("python", "PYTHON", "   ") == ("python",)
    assert collect_tags("tag1", "tag2", "tag1") == ("tag1", "tag2")

    print("Все assert-проверки пройдены успешно!")

    print(build_report("давид", [90, 95, 100], precision=1, prefix="Отчет"))

    marks = [80, 85, 90]
    config = {"precision": 2, "prefix": "Успеваемость"}
    print(build_report("дарья", marks, **config))

    tags_list = ["  python ", "labs", "PYTHON"]
    print("Теги через *:", collect_tags(*tags_list))

    topic_after, inner_res = outer_function()
    print("LEGB:", inner_res)
    print("topic после nonlocal:", topic_after)

    print("buggy:", buggy_add_result(1), buggy_add_result(2))
    print("fixed:", fixed_add_result(1), fixed_add_result(2))

    scores = [50.0, 70.0, 90.0]
    bonus = apply_to_results(lambda x: x + 5.0, scores)
    print("С бонусом (+5):", bonus)

    pass_60 = make_threshold_checker(60.0)
    pass_80 = make_threshold_checker(80.0)
    for s in scores:
        print(f"Балл {s}: >=60 -> {pass_60(s)}, >=80 -> {pass_80(s)}")
