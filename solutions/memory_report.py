import sys
import tracemalloc


def measure(name, create):
    tracemalloc.start()
    obj = create()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    count = len(obj) if hasattr(obj, "__len__") else 1
    return [name, count, sys.getsizeof(obj), current, peak]



changes = []

def grow():
    a = []
    size = sys.getsizeof(a)

    for i in range(100):
        a.append(i)
        new_size = sys.getsizeof(a)
        if new_size != size:
            changes.append((len(a), new_size))
            size = new_size

    return a



results = [
    measure("Пустой список", lambda: []),
    measure("Список из 10 чисел", lambda: list(range(10))),
    measure("Кортеж", lambda: tuple(range(10))),
    measure("Строка", lambda: "abcdefghij"),
    measure("Число", lambda: 100),
    measure("None", lambda: None),
    measure("Рост списка", grow),
    measure("Список 100000", lambda: list(range(100_000))),
    measure("Range 100000", lambda: range(100_000))
]


for name, count, size, current, peak in results:
    print("\nСценарий:", name)
    print("Элементов:", count)
    print("Размер объекта:", size, "байт")
    print("Текущая память:", round(current / 1024, 2), "КБ")
    print("Пиковая память:", round(peak / 1024, 2), "КБ")

print("\nРост списка:", changes)


list_peak = results[-2][4]
range_peak = results[-1][4]

if range_peak > 0:
    print("Отношение пиков:",
          round(list_peak / range_peak, 2))
else:
    print("Отношение пиков вычислить нельзя")