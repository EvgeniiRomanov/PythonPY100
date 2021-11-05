if __name__ == "__main__":

    i = 9
    lenght = len(str(i**2)) + 3
    wight = len(str(i)) + 3

    headers = ' ' * wight + ' ' + ''.join([str(x).rjust(lenght) for x in range(1, i+1)])
    dashes = ' ' * wight + ':' + '-' * lenght * i



    body = ''

    for row in range(1, i+1):
        #print("Строка", row, end=' ')
        body += str(row).rjust(wight) + ':'
        for column in range(1, i+1):
            #print("Столбец", column, end=' ')
            body += str(row * column).rjust(lenght)
        body += '\n'
        #print()

    print("\n".join([headers, dashes, body]))



    # matrix = []
    #
    # for row in range(1, 10):
    #     for col in range(1, 10):
    #         matrix[row][col] = row * col
    #
    # print(matrix)
    #
    # str_ = 'car'
    # widht = 5
    # print(str_.rjust(widht, "-"))
    # print(str_.ljust(widht, "-"))
    # print(f"{str_:5{widht}}")
    # print(f"{str_:*^10}")
    # print(f"{str_:*<10}")
    #
    # # dict1 = {}
    # dict2 = {
    #     "apple": 1,
    #     "orange": '3e',
    #     "Cocos": 10
    # }
    # for j in dict2:
    #     print(j, type(j))
    #
    # for j,i in dict2.items():
    #     print(j, type(j), i,type(i))
    #
    # for j in dict2.items():
    #     print((j),type(j))



    #
    # dict3 = {j: j+1 for j in range(1, 10)}
    # print(dict3)


