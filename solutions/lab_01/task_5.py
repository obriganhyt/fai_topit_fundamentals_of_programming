"""Консольная программа для расчёта параметров эксперимента."""

name = input("Введите своё имя: ") 
experiment = input("Введите название эксперимента: ") 
runs = int(input("Введите количество запусков: ")) 
dur = float(input("Введите длительность одного запуска в секундах: ")) 
a = float(input("Введите действительную часть коэффициента: ")) 
b = float(input("Введите мнимую часть коэффициента: "))


seconds = runs * dur
minutes = seconds/60
coef = complex(a,b)
coef2 = a**2 + b**2
maderuns = bool(runs)


print()
print("=" * 35)
print(f"ЭКСПЕРИМЕНТ: {experiment}")
print(f"Исследователь: {name}")
print(f"Запуски: {runs}")
print(f"Общее время: {seconds:.2f} с ({minutes:.2f} мин)")
print(f"Коэффициент: {coef}")
print(f"Квадрат модуля: {coef2:.2f}")
print(f"Есть выполненные запуски: {maderuns}")
print("=" * 35)


print("Типы введённых значений:")
print(type(name).__name__)
print(type(experiment).__name__)
print(type(runs).__name__)
print(type(dur).__name__)
print(type(a).__name__)
print(type(b).__name__)
