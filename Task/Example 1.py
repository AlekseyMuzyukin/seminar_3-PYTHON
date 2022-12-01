lst = list(range(1, 6))
sum = 0
for i in range(len(lst)):
    if i % 2 != 0:
        sum += lst[i]
print(f'В списке {lst} сумма нечётных = {sum}')