skaitli = [int(sk) for sk in input().split()]

summa = 0
for i in range(len(skaitli)):
    summa += skaitli[i - 1]
print(summa)