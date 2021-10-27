def find_number():

    num_list = []
    while True:
        a = int(input("Введите целое число: "))
        if 3 <= a <= 13:
            num_list.append(a)
        elif 0 <= a < 3 or a > 13:
            continue
        else:
            break
    return print(num_list)
