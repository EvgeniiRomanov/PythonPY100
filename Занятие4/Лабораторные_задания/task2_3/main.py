if __name__ == "__main__":

    a = 49999999999
    num_list = [int(x) for x in str(a)]
    print(sum(num_list))
    if (len(str(sum(num_list)))) == 2:
         print("Число из двух знаков")
    else:
         print("Число не из двух знаков")


