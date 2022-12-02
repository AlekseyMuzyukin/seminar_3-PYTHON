a = int(input('Введите число '))
n = []
while a > 0:
    n.append(a % 2)
    a //= 2
print(*n[::-1], sep = '')
