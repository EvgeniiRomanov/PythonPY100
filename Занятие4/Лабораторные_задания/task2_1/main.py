def func_1():

    a = str(12345)
    num_list = [int(x) for x in str(a)]
    print(f"1. Список цифр числа {num_list}")
    print(f"2. {sum(num_list)}")
    print("3.", sum([x for x in num_list if x % 2 == 0]))
    print("4.", len(num_list))
    print(f"5. min = {min(num_list)} max = {max(num_list)}")
    print("6неч.", [x for x in num_list if num_list.index(x) % 2 == 0])
    print("6чет.", [x for x in num_list if num_list.index(x) % 2 != 0])
    print("7.", str(num_list[0] - num_list[-1]))
    print(f"8. Число {min(num_list)} index: {num_list.index(min(num_list))})")

if __name__ == "__main__":
    # Write your solution here
    func_1()
    pass
   # print(list(str(num1)))
   #
   #  # Конструкция для разбития числа на цифры
   #  digits_list = [int(d) for d in str(num1)]
   #  print(digits_list)
   #
   #  join_num = "".join([str(d) for d in digits_list])
   #  print(int(join_num))