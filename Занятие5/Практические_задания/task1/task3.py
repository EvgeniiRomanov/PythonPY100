# 3. Требуется создать функцию list_sort(lst), которая сортирует список чисел
# по убыванию их абсолютного значения.
def list_sort(lst):

    for i in range(len(lst)):
        lst[i] = abs(lst[i])

    lst.sort()
    lst.reverse()

    return print(lst)

if __name__ == "__main__":

    a = [1, 5, 7, -8, -4, -9, 0, -57, 61]
    list_sort(a)