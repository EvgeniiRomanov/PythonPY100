if __name__ == "__main__":

    a = 49
    num_list = [int(x) for x in str(a)]
    a_4 = num_list.count(4)
    a_9 = num_list.count(9)
    a_8 = num_list.count(8)

    if (a_4 and a_8) or a_9:
        print("Да")
    else:
        print("Нет")

    #a = 4 and 8 in set(num_list) or 9 in set(num_list)
