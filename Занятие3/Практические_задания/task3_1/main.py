def remove_whitespace(str_):

    word_str = str_.split(" ")
    #print(word_str, type(word_str))
    word_str_no = []
    #str1 = " "
    for word in word_str:
        if word != "":
            word_str_no.append(word)
    #print(word_str_no, type(word_str_no))
    #str1 = " ".join(word_str_no)
    #print(str1, type(str1))
    return  (" ".join(word_str_no))

if __name__ == "__main__":
    str_with_space = "    123.    test   print test11    "  # исходная строка
    abc = print(remove_whitespace(str_with_space), type(remove_whitespace(str_with_space)))