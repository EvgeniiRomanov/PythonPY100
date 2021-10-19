if __name__ == "__main__":
    list_ = [15, 34, -78, 66, 12, 78, -8, 103, 101, -7]

    a = list_[0]
    b = list_[0]

    for index, value in enumerate(list_):
        if value >= a:
            a = value
            i = index
    list_[0] = a
    list_[i] = b

    print(list_)