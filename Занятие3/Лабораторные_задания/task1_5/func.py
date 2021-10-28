def find_sum():
    num_list = []
    while True:
        a = int(input("Введите целое число, когда введете 0 подсчитаем сумму"
                      "положительных чисел: "))
        if a > 0:
            num_list.append(a)
        elif a < 0:
            continue
        else:
            break
    return print(sum(num_list))


#find_sum()
