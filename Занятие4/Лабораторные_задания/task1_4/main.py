def func1(n, m):

    list_ = range(n, m)
    x = sum(list_)/len(list_)

    return [i for i in list_ if i > x]

if __name__ == "__main__":
    # Write your solution here
    print(func1(2, 9))