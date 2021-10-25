def remove_whitespace(str_):

    word_str = str_.split(" ")
    word_str_no = []

    for word in word_str:
        if word != "":
            word_str_no.append(word)

    #abc = str(word_str_no)
    return  word_str_no

if __name__ == "__main__":
    str_with_space = "    123.    test   print test11    "  # исходная строка
    print(remove_whitespace(str_with_space), type(remove_whitespace(str_with_space)))
