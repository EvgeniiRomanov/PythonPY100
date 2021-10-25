def fuctorial_(value_):

    count = 1
    factor_ = 1

    while count <= value_:
        factor_ *= count
        count +=1
        #(factor_)
    return factor_

a = fuctorial_(3)
print(a)