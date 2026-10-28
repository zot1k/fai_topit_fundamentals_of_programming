def validate_input(score: int, absences: int) -> tuple[bool, str]:
    if not (0 <= score <= 100):
        return False, f"Ошибка: балл {score} вне [0, 100]"
    if not (0 <= absences <= 5):
        return False, f"Ошибка: пропуски {absences} вне [0, 5]"
    return True, ""


def determine_level(score: int, absences: int) -> str:
    if score >= 90:
        level = "отличный"
    elif score >= 75:
        level = "хороший"
    elif score >= 60:
        level = "удовлетворительный"
    else:
        level = "недостаточный"

    if absences > 3:
        levels = ["недостаточный", "удовлетворительный", "хороший", "отличный"]
        idx = levels.index(level)
        level = levels[max(0, idx - 1)]

    return level


def describe_work(work_type: str) -> str:
    match work_type:
        case "exam":
            return "экзаменационная работа"
        case "project":
            return "проектная работа"
        case "practice":
            return "практическая работа"
        case _:
            return "неизвестный тип работы"


def classify_student(score: int, work_type: str, absences: int) -> str | None:
    ok, err = validate_input(score, absences)
    if not ok:
        print(err)
        return None
    return f"{describe_work(work_type)} | Балл: {score} | Пропусков: {absences} | Уровень: {determine_level(score, absences)}"


def process_batch(records: list[tuple[int, str, int]]) -> dict[str, int]:
    counts = {"отличный": 0, "хороший": 0, "удовлетворительный": 0, "недостаточный": 0}
    for score, wtype, abs_cnt in records:
        res = classify_student(score, wtype, abs_cnt)
        if res:
            print(res)
            counts[determine_level(score, abs_cnt)] += 1

    print("\nИтоги по уровням:")
    for lvl, cnt in counts.items():
        print(f"{lvl}: {cnt}")
    return counts


if __name__ == "__main__":
    test_cases = [
        (0, "practice", 0),
        (59, "practice", 2),
        (60, "project", 1),
        (74, "exam", 3),
        (75, "practice", 0),
        (89, "project", 2),
        (90, "exam", 1),
        (100, "project", 0),
        (90, "exam", 4),
        (60, "practice", 4),
    ]

    print("Проверка тестов:")
    for s, w, a in test_cases:
        print(classify_student(s, w, a))

    students = [
        (95, "exam", 1),
        (82, "project", 0),
        (70, "practice", 2),
        (50, "exam", 0),
        (92, "project", 4),
        (76, "practice", 4),
        (65, "exam", 5),
        (45, "project", 4),
        (100, "exam", 0),
        (88, "practice", 3),
        (59, "project", 1),
        (60, "exam", 0),
    ]

    print("\nПакетная обработка:")
    process_batch(students)
