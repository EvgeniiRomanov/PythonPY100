def polin_number(a1):

    #a = -66
    #num_a = [int(x) for x in str(a)]

    num_a = str(abs(a1))

    for i in range(len(num_a)-1):
        if num_a[i] != num_a[i+1]:
            return print(f"Цифры разные")

    return print(f"Цифры одинаковые")

    # for i in num_a:
    #     if num_a.count(i) != len(num_a):
    #         return print(f"Цифры разные ")
    #
    # return print(f"Цифры одинаковые")

if __name__ == "__main__":

     a1 = int(input("Введите целое число?"))
     polin_number(a1)
