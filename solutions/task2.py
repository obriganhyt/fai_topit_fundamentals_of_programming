import copy

original = [
    ["Python", 5],
    ["Algorithms", 4],
]

alias = original
shallow = original.copy()
deep = copy.deepcopy(original)

def structure(stage):
    print(f"\n===== {stage} =====")

    print("original:", original)
    print("alias:   ", alias)
    print("shallow: ", shallow)
    print("deep:    ", deep)

    print("\nИдентификаторы внешних списков:")
    print("original:", id(original))
    print("alias:   ", id(alias))
    print("shallow: ", id(shallow))
    print("deep:    ", id(deep))

    print("\nИдентификаторы первого вложенного списка:")
    print("original:", id(original[0]))
    print("alias:   ", id(alias[0]))
    print("shallow: ", id(shallow[0]))
    print("deep:    ", id(deep[0]))

    print("\nИдентификаторы первой оценки:")
    print("original:", id(original[0][1]))
    print("alias:   ", id(alias[0][1]))
    print("shallow: ", id(shallow[0][1]))
    print("deep:    ", id(deep[0][1]))


original.append(["Databases", 5])
structure("После original.append()")

original[0][1] = 3
structure("После изменения первой оценки")


print("\n===== Матрица с ошибкой =====")

wrong_matrix = [[0] * 3] * 3
wrong_matrix[0][0] = 1
print(wrong_matrix)

print("Идентификаторы строк:")
for row in wrong_matrix:
    print(id(row))


print("\n===== Правильная матрица =====")

correct_matrix = [[0] * 3 for _ in range(3)]
correct_matrix[0][0] = 1
print(correct_matrix)

print("Идентификаторы строк:")
for row in correct_matrix:
    print(id(row))