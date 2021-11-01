def func_str(str_1):

    char_dict1 = {}
    str_1 = str_1.lower()

    for i in str_1:
        if i.isalpha():
            if i in char_dict1:
                char_dict1[i] += 1
            else:
                char_dict1[i] = 1

    return char_dict1

def func_str_5(dict_b):

    c = sum(dict_b.values())
    for j in dict_b:
        dict_b[j] = round((dict_b[j] / c) * 100, 2)

    return dict_b


if __name__ == "__main__":
    main_str = """
        Данное предложение будет разбиваться на отдельные слова. 
        В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
        Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
    """
    # Задание 1
    char_dict = {}
    main_str = main_str.lower()

    for i in main_str:
        if i.isalpha():
            if i in char_dict:
                char_dict[i] += 1
            else:
                char_dict[i] = 1

    print(f"Задание 1. {char_dict}")
    # Задание 2-4
    a = input("Задание 2-4. Введите строку:")
    b = func_str(a)
    print(f"Задание 2. {b}")
    # Задание 5
    b_5 = func_str_5(char_dict)
    print(f"Задание 5. {b_5}")


    # from collection import Counter так и так как просит Алексей