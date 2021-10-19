A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
c = int(input("Введите число C: "))

if (A < 45 and B >= 45 and c >= 45) or (A >= 45 and B < 45 and c >= 45) or (A >= 45 and B >= 45 and c < 45):
    print("Одно из введенных чисел меньше 45")
else:
    print("Все числа больше или меньше 45")
