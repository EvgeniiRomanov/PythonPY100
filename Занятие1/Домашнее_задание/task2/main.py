if __name__ == "__main__":
    # Write your solution here
    # Если считать, что среднее время берется одно для всех
    time_1_task = int(input("Введите время в минутах, затрачиваемое на выполнение одной задачи: "))
    time_all_task = (time_1_task * 10) / 60
    #print(time_all_task)
    print("Примерное время на решение всех задач в часах: " + str(round(time_all_task, 0)))


