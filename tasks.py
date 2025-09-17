# Арифметикалық операциялар
print("Арифметикалық операциялар:")
a = 5 + 3
b = 10 - 4
c = 7 * 2
d = 2 ** 3
e = 9 / 2
f = 9 // 2
g = 9 % 2

print("5 + 3 =", a)
print("10 - 4 =", b)
print("7 * 2 =", c)
print("2 ** 3 =", d)
print("9 / 2 =", e)
print("9 // 2 =", f)
print("9 % 2 =", g)

print("\nЦиклдар:")
# while
i = 1
while i <= 5:
    print("while:", i)
    i += 1

# for
for j in range(1, 6):
    print("for:", j)

print("\nСписокпен тапсырмалар:")

# 1. Списокты кері шығару
lst = [1, 2, 3, 4, 5]
print("Кері тізім:", lst[::-1])

# 2. Сортировка абсолют мәні бойынша кему ретімен
def list_sort(lst):
    return sorted(lst, key=abs, reverse=True)

print("Сортировка:", list_sort([3, -10, 5, -7, 2]))

# 3. Бірінші және соңғы элементтерді ауыстыру
def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

print("Ауыстырылған:", change([1, 2, 3, 4]))
