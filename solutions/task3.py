import sys

data = [1, 2, 3]
print("После создания:", sys.getrefcount(data))

alias = data
print("После создания alias:", sys.getrefcount(data))

container = [data]
print("После помещения в контейнер:", sys.getrefcount(data))

del alias
print("После del alias:", sys.getrefcount(data))

container.clear()
print("После очистки контейнера:", sys.getrefcount(data))

#эксперимент
 
import weakref


class Record:
    pass


record = Record()
weak_record = weakref.ref(record)

print("До удаления объекта:", weak_record())

del record

print("После удаления объекта:", weak_record())



#Практическое задание

registry = weakref.WeakValueDictionary()


record1 = Record()
record2 = Record()
record3 = Record()


registry["first"] = record1
registry["second"] = record2
registry["third"] = record3


del record3

print("После удаления record3:")
print("Записи в реестре:", list(registry.keys()))


del record1

print("\nПосле удаления record1:")
print("Записи в реестре:", list(registry.keys()))

print("\nОставшиеся записи:")
for key in registry:
    print(key, "— объект существует")