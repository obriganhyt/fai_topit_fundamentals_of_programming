#часть 1
import sys

empty_list = []
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
text = "asdfghjkl;"
number = 50
nothing = None

print("Пустой список:", sys.getsizeof(empty_list), "байт")
print("Список из 10 чисел:", sys.getsizeof(numbers), "байт")
print("Кортеж из 10 чисел:", sys.getsizeof(numbers_tuple), "байт")
print("Строка из 10 символов:", sys.getsizeof(text), "байт")
print("Целое число:", sys.getsizeof(number), "байт")
print("Объект None:", sys.getsizeof(nothing), "байт")

#часть 2

numb = []
previous_size = sys.getsizeof(numb)

print("Длина:", len(numb), "Размер:", previous_size, "байт")

for i in range(100):
    numb.append(i)
    current_size = sys.getsizeof(numb)

    if current_size != previous_size:
        print("Длина:", len(numb), "Размер:", current_size, "байт")
        previous_size = current_size

#часть 3

import tracemalloc

tracemalloc.start()

numbers = list(range(100_000))

current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Список list(range(100_000)):")
print("Текущая память:", current / 1024, "КБ")
print("Пиковая память:", peak / 1024, "КБ")

del numbers




tracemalloc.start()

numbers = range(100_000)

current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("\nОбъект range(100_000):")
print("Текущая память:", current / 1024, "КБ")
print("Пиковая память:", peak / 1024, "КБ")

del numbers
