def step_func1(a, b, procent, S):
#def step_func1():

    # S = 400
    # a = 100
    # b = 200
    # procent = 5
    count = 0

    while True:
        S += a
        S -= b
        if S <= 0:
            #print(count)
            break
        else:
            b += b * procent/100
            count += 1

    return print(f"Студент проживет {count} целых месяцев")


#step_func1()
