sum = int(input("Введите сумму: "))
compos = int(input("Введите произведение: "))

for x in range(1,1000):
    for y in range(1,1000):
        if(x+y == sum) and (x*y == compos):
            print(f"x = {x}, y = {y}")