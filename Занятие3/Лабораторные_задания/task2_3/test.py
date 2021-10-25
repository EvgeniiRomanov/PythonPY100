def poisk_slov():

    str1 = input("Введите строку различных слов через пробел (слова могут повторятся): ")
    list_str1 = str1.split(" ")
    #list_str2 = []

    for word in list_str1:
        if list_str1.count(word) == 1:
            #list_str2.append(word)
            print(word)
    return None
