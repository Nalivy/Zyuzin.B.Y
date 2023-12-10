# -- coding: utf-8 --

## Задание 2

def calc(a,b):
    if a < b:
        return a
    else:
        return calc(a - b, b)

def nums():
    a = int(input('Введите число A: '))
    b = int(input('Введите число B: '))
    if b == 0:
        print('Деление на 0')
        return nums()
    else:
        return a,b

def main():
    a, b = nums()
    result = calc(a,b)
    print(f'Остаток от деления A на B равен: {result}')

main()