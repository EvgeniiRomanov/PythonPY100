def main(number):

    sum =  0
    count_list = 0
    list_ = list(range(1, 20))

    while True:
        for value in list_:
            sum += value**2
            count_list += 1
            if sum > number:
                print(sum, count_list)
                break
        break
    return (count_list-1)


#b = main_new(500)
#print(b)