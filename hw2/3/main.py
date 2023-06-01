number = int(input("Введите число: "))

temp = 0
while(2 ** temp <= number):
    print(f"{2 ** temp} ")
    temp += 1