#1. Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент.
#   В исходном списке минимум 2 элемента.
def change(lst):

    lst1 = lst.copy()
    lst[0], lst[-1] = lst1[-1], lst1[0]

    return print(lst)

if __name__ == "__main__":

    list_a = list(input("Введите строку:"))
    change(list_a)