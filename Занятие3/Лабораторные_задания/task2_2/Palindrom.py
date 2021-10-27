def palindrom_func(str1):

    str1 = str1.lower()
    str1 = str1.replace(" ", "")
    #str2 = str1[::-1]
    str2 = "".join(reversed(str1))
    #print(str1, type(str1), str2, type(str2))
    if str1 == str2:
        return print("Палиндром")
    else:
        return print("Не Палиндром")

#--------Заморочился по началу--------------------
   # # Write your solution here

    # str1 = list(str1.lower())               # в нижний рег и в список
    # str2 = str1.copy()
    # str3 = []
    # str4 = []
    #
    # str1.reverse()                          # разворачиваем список
    # for index in range(len(str1)):
    #     if str1[index].isalnum():           # если символ или цифра
    #         str3.append(str1[index])        # пишем в список
    # # for index in range(len(str2)):            # можно так
    # #     if str2[index].isalnum():
    # #         str4.append(str2[index])

    # for index in range(len(str2)):              # можно так
    #     if str2[index] != " ":
    #         str4.append(str2[index])
    #
    # if str3 == str4:
    #     return print("Строка Палиндром")
    # else:
    #     return print("Обычная строка")
#------------------------------------------------------------------
#palindrom_func("Аргентина манит негра")