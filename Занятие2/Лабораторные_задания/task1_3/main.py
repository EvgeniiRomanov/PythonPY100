A = int(input("Введите число А: "))
B = int(input("Введите число B: "))

sum1 = A**2 + B**2
sum2 = (A + B) ** 2
if sum1 > sum2:
    print("Сумма квадратов чисел больше квадрата их суммы")
elif sum1 < sum2:
    print("Квадрат суммы чисел больши суммы квадратов этих же чисел")
else:
    print("Квадрат суммы чисел равен сумме квадратов")