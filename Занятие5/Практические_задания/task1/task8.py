# 8. Требуется определить индексы первого и последнего вхождения буквы в строке.
# Для этого нужно написать функцию first_last(letter, st), включающую 2 параметра:
# letter – искомый символ, st – целевая строка.
# В случае отсутствия буквы в строке, нужно вернуть кортеж (None, None),
# если же она есть, то кортеж будет состоять из первого и последнего
# индекса этого символа.

def first_last(letter, st):
#-------------------------------1 методами строк коротко и ясно-----------------------------
    # start_index = None
    # end_index = None
    #
    # if st.count(letter) >= 1:
    #     start_index = st.find(letter)
    #     end_index = st.rfind(letter)
    #
    # return (start_index, end_index)
#-----------------------------------2 через список и 1 цикл ---------------------------------------------

    a = [i for i in st]
    b = []
    start_index = None
    end_index = None

    # for j in range(len(a)):
    #     if a[j] == letter:
    #         b.append(j)

    [b.append(j) for j in range(len(a)) if a[j] == letter]

    if len(b) == 0:
        return start_index, end_index
    elif len(b) == 1:
        return b[0], b[0]
    else:
        return b[0], b[-1]
#-----------------------------------через 2 списка, 2 цикла если строка большая возможно break вывалит раньше----------
    # a = [i for i in st]
    # b = []
    # for j in range(len(a)):
    #     if a[j] == letter:
    #         start_index = j
    #         print(f"Индекс с начала равен {start_index}")
    #         break
    #     else:
    #         start_index = None
    #
    # end_index = None
    # numbers_of_letter = a.count(letter)     #Если вхождение letter = 1, во второй цикл не идем
    #
    # if numbers_of_letter > 1:
    #     for j in range(len(a)):
    #         if a[-j-1] == letter:
    #             end_index = -j-1
    #             print(f"Индекс с начала равен {end_index}")
    #             break
    #
    # print(st)
    #
    # return (start_index, end_index)
#---------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    a_letter = input("Введите букву: ")
    a_st = input(f"Введите строку в которой искать букву {a_letter}: ")
    print(first_last(a_letter, a_st))