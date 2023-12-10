# -- coding: utf-8 --

## Задание 2

def nums(lst):
    x = int(input('Введите число последовательности (0 для окончания): '))
    if x == 0:
        return lst
    else:
        lst.append(x)
        return nums(lst)

def second_larset(lst,attemp):
    largest = max(lst)
    if attemp == 1:
        return largest
    else:
        lst.remove(largest)
        attemp += 1
        return second_larset(lst,attemp)

numbers = []

print(f'Второе по величине число последовательности: {second_larset(nums(numbers),0)}')