#if __name__ == "__main__":

# def main_new(number):
#
#     sum =  0
#     count_list = 0
#     list_ = list(range(1, 20))
#
#     while True:
#         for value in list_:
#             sum += value**2
#             count_list += 1
#             if sum > number:
#                 print(sum, count_list)
#                 break
#         break
#     return (count_list-1)

from test import main
import test

if __name__ == "__main__":

    b = main(number = 500)
    print(b)