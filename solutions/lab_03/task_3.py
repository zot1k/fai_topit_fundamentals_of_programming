def add_submission(
    student: str,
    lab: str,
    score: int,
    all_students: set,
    all_labs: set,
    student_attempts: dict,
    best_scores: dict,
    attempt_counts: dict,
):
    all_students.add(student)
    all_labs.add(lab)
    student_attempts.setdefault(student, []).append((lab, score))
    key = (student, lab)
    best_scores[key] = max(best_scores[key], score) if key in best_scores else score
    attempt_counts[key] = attempt_counts.get(key, 0) + 1


def handle_query(query: str, student_attempts: dict, best_scores: dict, attempt_counts: dict):
    parts = query.strip().split()
    if not parts:
        return "Пустой запрос"

    cmd = parts[0].lower()
    match cmd:
        case "student":
            name = parts[1] if len(parts) > 1 else ""
            return f"Попытки {name}: {student_attempts.get(name, 'не найден')}"
        case "best":
            key = (parts[1], parts[2]) if len(parts) > 2 else ()
            return f"Лучший {key}: {best_scores.get(key, 'нет данных')}"
        case "attempts":
            key = (parts[1], parts[2]) if len(parts) > 2 else ()
            return f"Попыток {key}: {attempt_counts.get(key, 0)}"
        case "completed":
            lab = parts[1] if len(parts) > 1 else ""
            studs = [s for s, atts in student_attempts.items() if any(l == lab for l, _ in atts)]
            return f"Сдали {lab}: {studs}"
        case _:
            return f"Неизвестная команда: {cmd}"


if __name__ == "__main__":
    submissions = [
        ("anna", "lab_01", 5),
        ("boris", "lab_01", 4),
        ("anna", "lab_02", 5),
        ("daria", "lab_01", 3),
        ("boris", "lab_02", 5),
        ("anna", "lab_01", 4),
    ]

    students = set()
    labs = set()
    attempts = {}
    best = {}
    counts = {}

    for s, l, sc in submissions:
        add_submission(s, l, sc, students, labs, attempts, best, counts)

    print("Студенты:", students)
    print("Работы:", labs)
    print("Попытки:", attempts)
    print("Лучшие баллы:", best)
    print("Количество попыток:", counts)

    completed_both = {s for s, atts in attempts.items() if {"lab_01", "lab_02"}.issubset({l for l, _ in atts})}
    print("Сдали обе работы:", completed_both)

    print("\nДобавление daria lab_02:")
    add_submission("daria", "lab_02", 4, students, labs, attempts, best, counts)
    print("Лучший daria lab_02:", best.get(("daria", "lab_02")))

    print("\nЗапросы:")
    for q in ["student anna", "best anna lab_01", "attempts boris lab_02", "completed lab_01", "error test"]:
        print(f"> {q} -> {handle_query(q, attempts, best, counts)}")
