import copy


def print_structures(step_name, original, alias, shallow, deep):
    print(f"\n--- {step_name} ---")
    structures = {
        "original": original,
        "alias": alias,
        "shallow": shallow,
        "deep": deep,
    }

    for name, s in structures.items():
        first_inner_id = id(s[0]) if len(s) > 0 else "N/A"
        first_grade_id = id(s[0][1]) if len(s) > 0 and len(s[0]) > 1 else "N/A"
        print(f"[{name:8s}] Содержимое: {s}")
        print(f"           id(внешнего): {id(s)}")
        print(f"           id(s[0]):      {first_inner_id}")
        print(f"           id(s[0][1]):   {first_grade_id}")


def sequential_copy_experiment():
    print("=== Исследование способов копирования (alias, shallow, deep) ===")
    original = [
        ["Python", 5],
        ["Algorithms", 4],
    ]

    alias = original
    shallow = original.copy()
    deep = copy.deepcopy(original)

    print_structures("Исходное состояние", original, alias, shallow, deep)

    # Изменение 1: добавление элемента во внешний список original
    original.append(["Databases", 5])
    print_structures(
        "Изменение 1: original.append(['Databases', 5])",
        original,
        alias,
        shallow,
        deep,
    )

    # Изменение 2: изменение элемента во вложенном списке
    original[0][1] = 3
    print_structures(
        "Изменение 2: original[0][1] = 3", original, alias, shallow, deep
    )


def matrix_experiment():
    print("\n=== Исследование создания матриц ===")

    print("1. Ошибочный способ: wrong_matrix = [[0] * 3] * 3")
    wrong_matrix = [[0] * 3] * 3
    print(f"Исходная wrong_matrix: {wrong_matrix}")
    print(
        f"id(row 0): {id(wrong_matrix[0])}, id(row 1): {id(wrong_matrix[1])}, id(row 2): {id(wrong_matrix[2])}"
    )

    wrong_matrix[0][0] = 1
    print(f"После wrong_matrix[0][0] = 1: {wrong_matrix}")
    print(
        "Причина: умножение списка [* 3] копирует ССЫЛКУ на один и тот же список [0, 0, 0] трижды."
    )

    print("\n2. Правильный способ: correct_matrix = [[0] * 3 for _ in range(3)]")
    correct_matrix = [[0] * 3 for _ in range(3)]
    print(f"Исходная correct_matrix: {correct_matrix}")
    print(
        f"id(row 0): {id(correct_matrix[0])}, id(row 1): {id(correct_matrix[1])}, id(row 2): {id(correct_matrix[2])}"
    )

    correct_matrix[0][0] = 1
    print(f"После correct_matrix[0][0] = 1: {correct_matrix}")
    print(
        "Причина: списковое включение (list comprehension) создает НОВЫЙ список [0, 0, 0] на каждой итерации."
    )


if __name__ == "__main__":
    sequential_copy_experiment()
    matrix_experiment()
