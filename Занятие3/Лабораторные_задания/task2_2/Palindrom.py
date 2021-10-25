def palindrom_func(str1):
    # Write your solution here
    #str1 = "Аргентина манят негра"
    str1 = list(str1.lower())               # в нижний рег и в список
    #print(id(str1))                        # ВАЖНО, список нельзя присвоить просто, надо копировать
    str2 = str1.copy()
    #print(id(str2))
    str3 = []
    str4 = []

    str1.reverse()                          # разворачиваем список
    print(str1)
    print(str2)
    for index in range(len(str1)):
        if str1[index].isalnum():           # если символ или цифра
            str3.append(str1[index])        # пишем в список
    #print(str3)
    # for index in range(len(str2)):            # можно так
    #     if str2[index].isalnum():
    #         str4.append(str2[index])
    #print(str4)
    for index in range(len(str2)):              # можно так
        if str2[index] != " ":
            str4.append(str2[index])

    if str3 == str4:
        return print("Строка Палиндром")
    else:
        return print("Обычная строка")

#palindrom_func()