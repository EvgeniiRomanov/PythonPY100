if __name__ == "__main__":
    #list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    list_ = [4, 10, -1, -6, 8, 6, 9]

    new_list1 = len([i for i in list_ if i % 2 == 0])
    new_list2 = len([i for i in list_ if i % 2 != 0])

    if new_list1 > new_list2:
        print("Четных")
    else:
        print("Не Четных")