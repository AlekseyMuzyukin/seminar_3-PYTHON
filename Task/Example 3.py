import random
a = int(input('Введите размер списка '))
lst = [round(random.random(), 2) for i in range(a)]
lst2 = [round(i % 1, 2) for i in lst if i % 1 != 0]
answer = max(lst2) - min(lst2)
print(f'{lst} разница равна {answer}')
