def task(str1, str2, k):

    if str1[:k] == str2[:k]:
        return print("ДА")
    else:
        return print("НЕТ")

if __name__ == "__main__":
    str1_1 = input("Введите строку 1: ")
    str2_2 = input("Введите строку 2: ")
    k1 = int(input("Введите целое число одинаковых символов для проверки: "))
    task(str1_1, str2_2, k1)

