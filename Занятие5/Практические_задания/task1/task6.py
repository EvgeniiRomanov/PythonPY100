"""6. Дана строка в виде случайной последовательности чисел от 0 до 9.
 Требуется создать словарь, который в качестве ключей будет принимать данные
  числа (т. е. ключи будут типом int), а в качестве значений – количество этих
   чисел в имеющейся последовательности. Для построения словаря
    создайте функцию count_it(sequence), принимающую строку из цифр.
     Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.
     """
def count_it(sequence):

    char_dict1 = {}

    for i in sequence:
        if i in char_dict1:
            char_dict1[i] += 1
        else:
            char_dict1[i] = 1

    lst1 = sorted(char_dict1.items(), key = lambda elem: elem[1])
    lst1.reverse()
    return print(dict(lst1[:3]))

a = input("Введите число из любой последовательности цифр: ")

count_it(a)