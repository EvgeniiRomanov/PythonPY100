if __name__ == "__main__":

    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]

    ever = sum(list_)/len(list_)

    list1 = [round(i - ever, 2) for i in list_]
    print(list1)