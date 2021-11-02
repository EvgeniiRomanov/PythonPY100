# 9. На вход функция more_than_five(lst) получает список из целых чисел.
# Результатом работы функции должен стать новый список, в котором содержатся только те числа, которые больше 5 по модулю.

def more_than_five(lst):

    print(isinstance(lst, list))
    list_new = []

    # for i in lst:
    #     if abs(i) > 5:
    #         list_new.append(i)
    [list_new.append(abs(i)) for i in lst if abs(i) > 5]

    return print(list_new)

if __name__ == "__main__":

    a = [1, 5, -8, -4, -9, 0, -57, 61]
    more_than_five(a)