def prostoe_chislo(value_):

    #value_ = 8
    number = 2
    spisok_ = []

    while value_ > 1:
        if value_ % number == 0:
            spisok_.append(number)
            value_ //= number
        else:
            number += 1

    print(spisok_)

if __name__ == "__main__":
    # Write your solution here
    prostoe_chislo(15)


