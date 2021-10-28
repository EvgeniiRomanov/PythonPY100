if __name__ == "__main__":
    # Write your solution here
    speed_ = int(input("Введите скорость передачи по лок сети в байт/сек: "))
    time_ = int(input("Сколько времени в минутах скачивался файл?: "))
    coast = int(input("Какова стоимость одного Гб трафика в рублях ?: "))

    file_size = speed_ * time_ * 60     #size in Bytes
    file_size /= 1024**3                #size in GB
    pay_ = (file_size - 1) * coast

    if pay_ > 0:
        print("Размер загруженного файла в Гб: " + str(file_size))
        print("Размер оплаты за загруженный файл в рублях: " + str(round(pay_, 2)))
    else:
        print("Файл скачан бесплатно!")

