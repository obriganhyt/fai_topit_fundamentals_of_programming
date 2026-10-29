#a
a = 10
b = a

print(a, b)
print(id(a), id(b))

a += 1

print(a, b)
print(id(a), id(b))

#b
first = [10, 20]
second = first

print("1. После присваивания:")
print("first:", first)
print("second:", second)
print("id(first):", id(first))
print("id(second):", id(second))

second.append(30)

print("\n2. После second.append(30):")
print("first:", first)
print("second:", second)
print("id(first):", id(first))
print("id(second):", id(second))


second = [10, 20, 30]

print("\n3. После переназначения second:")
print("first:", first)
print("second:", second)
print("id(first):", id(first))
print("id(second):", id(second))

print("\n4. Сравнение списков:")
print("first == second:", first == second)
print("first is second:", first is second)


second.append(40)

print("\n5. После second.append(40):")
print("first:", first)
print("second:", second)
print("first == second:", first == second)
print("first is second:", first is second)

#Практическое задание

import copy


config1 = {
    "name": "Проект А",
    "participants": ["Артём", "Максим"],
    "launch_params": {
        "mode": "debug",
        "options": ["verbose", "test"]
    }
}

config2 = config1

print("=== До изменений ===")
print("config1:", config1)
print("config2:", config2)


config2["participants"].append("Юрий")
config2["launch_params"]["options"].append("logging")

print("\n=== После изменения config2 ===")
print("config1:", config1)
print("config2:", config2)

assert config1 is config2
assert config1["participants"] is config2["participants"]
assert config1["launch_params"] is config2["launch_params"]

print("\nРезультат: config1 и config2 используют общие объекты.")


config3 = copy.deepcopy(config1)

print("\n=== Независимая конфигурация до изменений ===")
print("config1:", config1)
print("config3:", config3)


config3["name"] = "Проект Б"
config3["participants"].append("Вероника")
config3["launch_params"]["options"].append("safe")

print("\n=== После изменения config3 ===")
print("config1:", config1)
print("config3:", config3)


assert config1 is not config3
assert config1["participants"] is not config3["participants"]
assert config1["launch_params"] is not config3["launch_params"]
assert (
    config1["launch_params"]["options"]
    is not config3["launch_params"]["options"]
)
assert "Ольга" not in config1["participants"]
assert "safe" not in config1["launch_params"]["options"]

print("\nВсе проверки assert пройдены!")
print("config1 и config3 независимы")

