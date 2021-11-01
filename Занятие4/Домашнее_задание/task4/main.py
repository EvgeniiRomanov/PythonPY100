def polin_number(a):

    num_a = [int(x) for x in str(a)]

    # if sum(num_a[:3]) == sum(num_a[3:]):
    #     print(f"Число {a} Счастливое")
    # else:
    #     print(f"Число {a} обычное")

    return [print(f"Число {a} Счастливое") if sum(num_a[:3]) == sum(num_a[3:]) else print(f"Число {a} обычное")]

if __name__ == "__main__":

    a = int(input("Введите шестизначное целое число?"))
    polin_number(a)
