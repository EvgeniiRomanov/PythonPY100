if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]

    new_list1 = len([i for i in list_ if i > list_[0]])
    print(new_list1)