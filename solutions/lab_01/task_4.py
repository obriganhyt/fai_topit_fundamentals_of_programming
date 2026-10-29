student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10

percent = completed / total * 100

print('1:', student[0], student[3])
print('2:',student[:4])
print('2:',student[5:])
print('3:',student.upper())
print('3:',student.lower())
print('4:', student[0] + "." + student[5] + ".")
print('5:',course[::-1])
print('6.1:', "%s — %s: %d/%d (%.1f%%)" % (student, course, completed, total, percent))
print('6.2:',"{} — {}: {}/{} ({:.1f}%)".format( student, course, completed, total, percent ))
print('6.3:',f"{student} — {course}: {completed}/{total} ({percent:.1f}%)")



symbol = 'Я'

print('7: Кодовая позиция:', ord(symbol))
print('Восстановленный символ:', chr(ord(symbol)))
print("UTF-8:", symbol.encode("utf-8"))
print("Длина UTF-8:", len(symbol.encode("utf-8")))

#symbol[0] = "А"