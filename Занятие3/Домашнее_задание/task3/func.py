def func1():

    str1 = input("Введите слова через один или несколько пробелов:")
    k = 0
    word_list = []
    str1_list = str1.split()

    for word in str1_list:
        if len(word) > k:
            word_list.clear()
            word_list.append(word)
            k = len(word)
        elif len(word) == k:
            word_list.append(word)
            k = len(word)

    return print(word_list)
