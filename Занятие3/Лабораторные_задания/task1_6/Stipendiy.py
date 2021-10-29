def step_func(a, b, procent, k):

    # a = 100
    # b = 300
    # procent = 3
    # k = 10
    doxod = a * k
    sum_rasxod = []

    while k > 0:
        sum_rasxod.append(b)
        b += b * procent/100
        k -= 1

    nexvatka = doxod - sum(sum_rasxod)
    #print(nexvatka)
    if nexvatka >= 0:
        return print("Богатый студент, денег на учебный год хватает!")
    else:
        return print(f"Для жизни на учебный год необходимо: {doxod - nexvatka:.1f} рублей")