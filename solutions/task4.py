import gc

first = []
second = []

first.append(second)
second.append(first)

print("first ссылается на second:", first[0] is second)
print("second ссылается на first:", second[0] is first)

print("Сборщик включен:", gc.isenabled())
print("Пороги поколений:", gc.get_threshold())
print("Статистика поколений:", gc.get_stats())

id1 = id(first)
id2 = id(second)
print("ID первого списка:", id1)
print("ID второго списка:", id2)


del first
del second

collected = gc.collect()
print("Удалено объектов:", collected)


#эксперимент
gc.disable()
print("\nАвтоматический сборщик отключен:", gc.isenabled())

a = []
b = []
a.append(b)
b.append(a)

c = []
d = []
c.append(d)
d.append(c)

del a, b, c, d

print("Удалено вручную:", gc.collect())


gc.enable()
print("Автоматический сборщик включен:", gc.isenabled())



#практическое задание
do = gc.collect()
print("Собрано объектов до создания графа:", do)


a = {"name": "A", "links": []}
b = {"name": "B", "links": []}
c = {"name": "C", "links": []}

a["links"].append(b)
b["links"].append(c)
c["links"].append(a)


d = {"name": "D", "links": []}

#
print("A ->", a["links"][0]["name"])
print("B ->", b["links"][0]["name"])
print("C ->", c["links"][0]["name"])
print("Независимый узел:", d["name"])

print("Узел D доступен:", d["name"] == "D")


del a, b, c


posle = gc.collect()
print("Собрано объектов после удаления графа:", posle)


print("Узел D всё ещё доступен:", d["name"] == "D")