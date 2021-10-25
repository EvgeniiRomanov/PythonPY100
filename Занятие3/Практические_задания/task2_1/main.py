def pow_func(base=2, pow_=3):

    sum_ = base
    while pow_ > 1:
        sum_ = sum_ * base
        pow_ -= 1
       # print(sum_)
    return sum_

if __name__ == "__main__":
    a = 2
    n = 5

    print(pow_func(a, n))
