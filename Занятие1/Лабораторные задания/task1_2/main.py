if __name__ == "__main__":
    # Write your solution here

    oklad = int(input("Введите доход в месяц: "))
    nalog = oklad * 0.13
    zarplata = oklad - nalog
    print("Налог: ", nalog, "Зарплата: ", zarplata)
