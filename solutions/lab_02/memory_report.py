import sys
import tracemalloc
from dataclasses import dataclass, asdict
from typing import List, Dict, Any


@dataclass
class ScenarioResult:
    scenario_name: str
    num_elements: int
    sizeof_bytes: int
    current_memory_kb: float
    peak_memory_kb: float


def measure_scenario(scenario_name: str, num_elements: int, builder_func) -> ScenarioResult:
    """Измеряет sys.getsizeof и tracemalloc для заданного сценария создания структуры."""
    tracemalloc.start()
    tracemalloc.reset_peak()

    obj = builder_func()

    sizeof_bytes = sys.getsizeof(obj)
    current_bytes, peak_bytes = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    current_kb = current_bytes / 1024
    peak_kb = peak_bytes / 1024

    return ScenarioResult(
        scenario_name=scenario_name,
        num_elements=num_elements,
        sizeof_bytes=sizeof_bytes,
        current_memory_kb=current_kb,
        peak_memory_kb=peak_kb,
    )


def generate_memory_report(n_elements: int = 100_000) -> Dict[str, Any]:
    """Собирает результаты измерений в структуру данных и возвращает итоговый отчет."""
    results: List[ScenarioResult] = []

    # Сценарий 1: Материализованный список list(range(N))
    res_list = measure_scenario(
        scenario_name="Materialized List [list(range(N))]",
        num_elements=n_elements,
        builder_func=lambda: list(range(n_elements)),
    )
    results.append(res_list)

    # Сценарий 2: Ленивый генератор range(N)
    res_range = measure_scenario(
        scenario_name="Lazy Generator [range(N)]",
        num_elements=n_elements,
        builder_func=lambda: range(n_elements),
    )
    results.append(res_range)

    # Сценарий 3: Кортеж tuple(range(N))
    res_tuple = measure_scenario(
        scenario_name="Materialized Tuple [tuple(range(N))]",
        num_elements=n_elements,
        builder_func=lambda: tuple(range(n_elements)),
    )
    results.append(res_tuple)

    # Вычисление отношения пикового объема двух основных сценариев (с защитой от деления на 0)
    range_mem = res_range.peak_memory_kb if res_range.peak_memory_kb > 0.001 else (res_range.sizeof_bytes / 1024)
    list_mem = res_list.peak_memory_kb if res_list.peak_memory_kb > 0 else (res_list.sizeof_bytes / 1024)
    ratio_list_vs_range = list_mem / range_mem if range_mem > 0 else 0

    report_data = {
        "num_elements": n_elements,
        "scenarios": [asdict(r) for r in results],
        "peak_memory_ratio_list_to_range": ratio_list_vs_range,
    }

    return report_data


def print_memory_report(report_data: Dict[str, Any]):
    """Печатает форматированный единый отчет на основе собранной структуры данных."""
    n = report_data["num_elements"]
    print("=" * 85)
    print(f"               ИТОГОВЫЙ СВОДНЫЙ ОТЧЕТ ИЗМЕРЕНИЙ ПАМЯТИ (N = {n:,})")
    print("=" * 85)
    header = f"{'Сценарий':<35} | {'Элементов':<10} | {'sizeof (B)':<10} | {'Текущая (KB)':<12} | {'Пиковая (KB)':<12}"
    print(header)
    print("-" * 85)

    for item in report_data["scenarios"]:
        name = item["scenario_name"]
        num = item["num_elements"]
        sz = item["sizeof_bytes"]
        cur = item["current_memory_kb"]
        pk = item["peak_memory_kb"]
        print(f"{name:<35} | {num:<10d} | {sz:<10d} | {cur:<12.2f} | {pk:<12.2f}")

    print("-" * 85)
    ratio = report_data["peak_memory_ratio_list_to_range"]
    print(
        f"Отношение пикового потребления (List / Range): {ratio:.2f}x (Список потребляет в {ratio:.1f} раз больше памяти!)"
    )
    print("=" * 85 + "\n")


if __name__ == "__main__":
    report = generate_memory_report(100_000)
    print_memory_report(report)
