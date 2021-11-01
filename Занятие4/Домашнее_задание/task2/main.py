
    # Условие не понятно, но видимо что в числе среди его цифр есть одинаковые

def polin_number(a):

    num_a = [int(x) for x in str(a)]
    num_b = set(num_a.copy())
    a_len = len(num_a)
    b_len = len(set(num_b))

    return [print(f"В числе {a} ЕСТЬ одинаковые цифры") if a_len != b_len else print(f"В числе {a} НЕТ одинаковых цифр")]


if __name__ == "__main__":
    a1 = int(input("Введите целое число?"))
    polin_number(a1)
