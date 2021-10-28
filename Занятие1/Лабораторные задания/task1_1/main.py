if __name__ == "__main__":
    DAYS_OF_YEAR = 365  # количество дней в году

    start_year = int(input("Введите год вашего рождения: "))  # TODO запросить у пользователя год рождения
    current_year = int(input("Введите текущий год: "))  # TODO запросить у пользователя текущий год

    years_old = (current_year - start_year)*365
    print(years_old)
    # TODO посчитать и распечатать количество прожитых дней
