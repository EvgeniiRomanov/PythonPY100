def func1(n, m):
    #n = 2
    #m = 3
    list_ = []
    for i in range (n, m+1):
        list_.append(i ** 2)

    return list_

if __name__ == "__main__":
    # Write your solution here
    print(func1(2, 5))
