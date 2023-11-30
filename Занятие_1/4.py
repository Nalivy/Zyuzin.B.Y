# -- coding: utf-8 --
second=float(input("Введите колличество секунд: "))
minuts=float(second / 60)
hours=float(second / 3600)
days=float(second / 86400)
print(f"Минуты: {'%.2f'% minuts}\nЧасы: {'%.4f'% hours}\nДни: {'%.5f'% days}")