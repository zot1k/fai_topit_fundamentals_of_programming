from typing import Any, Optional


def mean(values: list[float | int]) -> float:
    if not values:
        return 0.0
    total = 0.0
    for v in values:
        total += v
    return total / len(values)


def minimum(values: list[float | int]) -> Optional[float | int]:
    if not values:
        return None
    res = values[0]
    for v in values[1:]:
        if v < res:
            res = v
    return res


def maximum(values: list[float | int]) -> Optional[float | int]:
    if not values:
        return None
    res = values[0]
    for v in values[1:]:
        if v > res:
            res = v
    return res


def classify(score: float | int) -> str:
    if score >= 90:
        return "отличный"
    elif score >= 75:
        return "хороший"
    elif score >= 60:
        return "удовлетворительный"
    else:
        return "недостаточный"


def student_summary(name: str, results: list[int]) -> dict[str, Any]:
    if not results:
        return {
            "name": name,
            "results": [],
            "mean": 0.0,
            "min": None,
            "max": None,
            "category": "нет оценок",
        }

    s_mean = mean(results)
    return {
        "name": name,
        "results": list(results),
        "mean": s_mean,
        "min": minimum(results),
        "max": maximum(results),
        "category": classify(s_mean),
    }


def find_top_students(students: dict[str, list[int]]) -> list[tuple[str, float]]:
    if not students:
        return []

    valid = [(name, mean(res)) for name, res in students.items() if res]
    if not valid:
        return []

    best_mean = valid[0][1]
    for _, avg in valid[1:]:
        if avg > best_mean:
            best_mean = avg

    return [item for item in valid if abs(item[1] - best_mean) < 1e-9]


def group_summary(students: dict[str, list[int]]) -> dict[str, Any]:
    cats = {
        "отличный": 0,
        "хороший": 0,
        "удовлетворительный": 0,
        "недостаточный": 0,
        "нет оценок": 0,
    }

    students_info = {}
    all_scores = []

    for name, res in students.items():
        summary = student_summary(name, res)
        students_info[name] = summary
        cats[summary["category"]] += 1
        all_scores.extend(res)

    group_mean = mean(all_scores) if all_scores else 0.0
    leaders = find_top_students(students)

    ranking = sorted(
        students_info.values(),
        key=lambda x: (len(x["results"]) > 0, x["mean"]),
        reverse=True,
    )

    return {
        "students": students_info,
        "total_students": len(students),
        "group_mean": group_mean,
        "categories": cats,
        "leaders": leaders,
        "ranking": ranking,
    }


def format_report(student_data: dict[str, dict], group_data: dict) -> str:
    lines = []
    lines.append("=" * 60)
    lines.append("ОТЧЕТ ПО УСПЕВАЕМОСТИ ГРУППЫ")
    lines.append("=" * 60)
    lines.append(f"Количество студентов: {group_data['total_students']}")
    lines.append(f"Средний балл по группе: {group_data['group_mean']:.2f}")

    if group_data["leaders"]:
        leaders_str = ", ".join(f"{name} ({avg:.2f})" for name, avg in group_data["leaders"])
        lines.append(f"Лидеры: {leaders_str}")
    else:
        lines.append("Лидеры: нет данных")

    lines.append("-" * 60)
    lines.append("По категориям:")
    for cat, cnt in group_data["categories"].items():
        if cnt > 0:
            lines.append(f"  {cat}: {cnt}")

    lines.append("-" * 60)
    lines.append(f"{'Имя':<10} | {'Ср. балл':<8} | {'Min':<5} | {'Max':<5} | {'Категория':<16}")
    lines.append("-" * 60)

    for item in group_data["ranking"]:
        min_v = str(item["min"]) if item["min"] is not None else "—"
        max_v = str(item["max"]) if item["max"] is not None else "—"
        lines.append(
            f"{item['name']:<10} | {item['mean']:<8.2f} | {min_v:<5} | {max_v:<5} | {item['category']:<16}"
        )

    lines.append("=" * 60)
    return "\n".join(lines)


if __name__ == "__main__":
    students = {
        "Анна": [78, 91, 84, 88],
        "Борис": [60, 72, 68],
        "Дарья": [95, 93, 97, 90],
        "Илья": [55, 61],
    }

    g_data = group_summary(students)
    print(format_report(g_data["students"], g_data))

    scenarios = [
        ("1. Базовый набор", students),
        ("2. Один студент", {"Виктор": [85, 90, 88]}),
        ("3. Несколько лидеров", {"Алиса": [90, 100], "Максим": [92, 98], "Олег": [80, 85]}),
        ("4. Пустая группа", {}),
        ("5. Студент без результатов", {"Елена": [90, 95], "Николай": []}),
        ("6. Граничные значения", {"С59": [59], "С60": [60], "С74": [74], "С75": [75], "С89": [89], "С90": [90]}),
    ]

    print("\nПроверка 6 сценариев:")
    for name, data in scenarios:
        print(f"\n--- {name} ---")
        res = group_summary(data)
        print(format_report(res["students"], res))
