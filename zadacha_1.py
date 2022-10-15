# Наптшите программу, которая принемает на вход число и показывае сумму цифр.

s = 0
number = input("Введите число: ")
res = list(map(int, [ch for ch in number if ch.isdigit()]))
for el in res:
      s += el
print(s)