def fuctorial_(value_):

    # count = 1
    # factor_ = 1
    #
    # while count <= value_:
    #     factor_ *= count
    #     count +=1
    factor_ = 1
    while value_ > 1:
        factor_ *= value_
        value_ -= 1

    return factor_

#print(fuctorial_(5))