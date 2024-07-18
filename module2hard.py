from random import randint
def trap(n):
    unique = ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                unique += str(i) + str(j)
    return f'{n} - {unique}\nПоздравляю, пароль верный'
n = int(input("Введите пароль: "))
result = trap(n)
print(result)
