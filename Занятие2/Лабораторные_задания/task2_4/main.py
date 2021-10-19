if __name__ == "__main__":
    # постарайтесь не использовать "магические" числа,
    # а по возможности дать переменным осмысленные названия и использовать их

    # slovo_ = list(input("Введите строку: "))
    slovo_ = list("Hello,world")
    # print(slovo_)
    prob_number = 5
    for value in range(len(slovo_)):
        print(" " * prob_number, slovo_[value])
        prob_number += 1
