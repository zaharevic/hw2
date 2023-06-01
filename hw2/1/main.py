from random import randint

def CoinsGenerate(n):
    tails = 0
    for i in range(0, n):
        temp = randint(0,1)
        if (temp == 1):
            tails += 1
    return tails

n = int(input("Введите количество монет: "))
tails = CoinsGenerate(n)
emblem = n - tails
print(f"Количество решек = {tails} \nКоличество орлов = {emblem}")
if(tails < emblem):
    print(f"Необходимо перевернуть: {tails}")
else:
    print(f"Необходимо перевернуть: {emblem}")