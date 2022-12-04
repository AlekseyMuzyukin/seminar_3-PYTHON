a = int(input('Введите число '))

fib1 = 0
fib2 = 1
i = 0
fibonachi_1 = []
fibonachi_2 =[]
while i < a - 1:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
    fibonachi_1.append(-fib2)
    fibonachi_2.append(fib2)
fibonachi = fibonachi_1[::-1] + [1, 0, 1] + fibonachi_2
print(fibonachi)
