# 7. Напишите функцию search_substr(subst, st), которая принимает 2 строки и
# определяет, имеется ли подстрока subst в строке st.
# В случае нахождения подстроки, возвращается фраза «Есть контакт!»,
# а иначе «Мимо!».
# Должно быть найдено совпадение независимо от регистра обеих строк.

def search_substr(subst, st):

    subst = subst.lower()
    st = st.lower()
    # if subst in st:
    #     print("Есть контакт")
    # else:
    #     print("Мимо")
    print("Есть контакт") if subst in st else print("Мимо")

    return

if __name__ == "__main__":

    subst = input("Введите подстроку: ")
    st = input("Введите строку в которой искать: ")
    search_substr(subst, st)