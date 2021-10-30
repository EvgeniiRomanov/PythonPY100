def func1(n, m):
    #n = 2
    #m = 3

    return [i ** 2 for i in range(n,m+1) if i % 2 != 0]

if __name__ == "__main__":
    # Write your solution here
    print(func1(2, 5))
