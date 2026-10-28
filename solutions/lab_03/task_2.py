import random


def analyze_data(data: list[int]):
    total = 0
    min_v = data[0]
    max_v = data[0]
    even_cnt = 0

    for x in data:
        total += x
        if x < min_v:
            min_v = x
        if x > max_v:
            max_v = x
        if x % 2 == 0:
            even_cnt += 1

    mean_v = total / len(data)
    above_mean_cnt = len([x for x in data if x > mean_v])

    return total, min_v, max_v, even_cnt, mean_v, above_mean_cnt


def linear_search(data: list[int], target: int) -> tuple[int, int]:
    for i, x in enumerate(data):
        if x == target:
            return i, i + 1
    return -1, len(data)


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def selection_sort(data: list[int]) -> list[int]:
    arr = list(data)
    n = len(arr)
    for i in range(n - 1):
        min_i = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr


def binary_search(data: list[int], target: int) -> tuple[int, int]:
    left = 0
    right = len(data) - 1
    comps = 0

    while left <= right:
        comps += 1
        mid = (left + right) // 2
        if data[mid] == target:
            return mid, comps
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comps


if __name__ == "__main__":
    measurements = [12, 15, 11, 18, 18, 9, 21, 15, 7, 18]
    total, min_v, max_v, even_cnt, mean_v, above_mean = analyze_data(measurements)

    print("measurements:")
    print("Сумма:", total)
    print("Минимум:", min_v)
    print("Максимум:", max_v)
    print("Четных:", even_cnt)
    print("Среднее:", mean_v)
    print("Больше среднего:", above_mean)

    print("\nЛинейный поиск:")
    print("18 ->", linear_search(measurements, 18))
    print("99 ->", linear_search(measurements, 99))

    print("\nПростые числа:")
    for num in [2, 3, 4, 17, 19, 25, 29, 97, 100]:
        print(f"{num}: {is_prime(num)}")

    print("\nСравнение числа сравнений:")
    for sz in [10, 100, 1000]:
        arr = selection_sort(random.sample(range(1, sz * 10), sz))
        for name, t in [("Первый", arr[0]), ("Середина", arr[sz // 2]), ("Последний", arr[-1]), ("Нет", -1)]:
            _, l_comp = linear_search(arr, t)
            _, b_comp = binary_search(arr, t)
            print(f"N={sz:<4} | {name:<10} | Линейный: {l_comp:<5} | Бинарный: {b_comp}")
