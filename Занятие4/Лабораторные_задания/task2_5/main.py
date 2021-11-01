def polin_number(a):

    #a = 123321

    num_a = [int(x) for x in str(a)]
    num_b = num_a.copy()
    num_b.reverse()
    if num_a == num_b:
        print(f"Число {a} является Палиндромом")
    else:
        print(f"Число {a} НЕ Палиндром")

    #print(num_a, num_b)

if __name__ == "__main__":

    a = int(input("Введите целое число?"))
    polin_number(a)