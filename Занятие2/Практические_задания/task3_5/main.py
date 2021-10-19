wind = int(input("Введите скорость ветра: "))

if wind in range(1, 5):
    print("слабый")
elif wind in range(5, 11):
    print("умеренный")
elif wind in range(12, 19):
    print("сильный")
elif wind > 19:
    print("ураганный")
else:
    print("Такого ветра быть не может!")
# TODO напишите с помощью if-elif-else условие проверки скорости ветра
