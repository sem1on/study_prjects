# Август и Беатриса играют в игру.
# Август загадал натуральное число от 1 до n.
# Беатриса пытается угадать это число,
# для этого она называет некоторые множества натуральных чисел.
# Август отвечает Беатрисе YES,
# если среди названных ею чисел есть задуманное
# или NO в противном случае.
# После нескольких заданных вопросов Беатриса запуталась в том,
# какие вопросы она задавала и какие ответы получила 
# и просит вас помочь ей определить, какие числа мог задумать Август.

# Формат ввода

# Первая строка входных данных содержит число n — наибольшее число,
# которое мог загадать Август. Далее идут строки, содержащие вопросы Беатрисы.
# Каждая строка представляет собой набор чисел, разделенных пробелами.
# После каждой строки с вопросом идет ответ Августа: YES или NO.
# Наконец, последняя строка входных данных содержит одно слово HELP.


n = int(input())
ans = set(range(1, n + 1))
q = 0
while True:
    q = input()
    if q == "HELP":
        break
    else:
        a = set(list(map(int, q.split())))
        q = input()
        if q == "YES":
            ans &= a
        else:
            ans -= a
ans = sorted(ans)
print(*ans)
