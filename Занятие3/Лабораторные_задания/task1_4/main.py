def infinity(epsilon = 0.0001):
    list_ = []
    n = 2

    while True:
        i = 1/n
        if i > epsilon:
            list_.append(i)
            n *= 2
        else:
            break

    return print(sum(list_))


infinity()