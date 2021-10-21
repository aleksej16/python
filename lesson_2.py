yes_dict = ['yes', 'Yes', 'да', 'Да', 'нуы', 'Нуы', 'lf', 'Lf', '1']


def sort_dict(vacc, len_vacc):
    if len_vacc % 2 != 0:
        len_vacc -= 1
    for x in range(0, len_vacc, 2):
     cur_txt = vacc[x]
     vacc[x] = vacc[x+1]
     vacc[x+1] = cur_txt
    return vacc


def task_1():
    my_list = [1, 34, 6538, True, False, "some text", 3.14]
    print(my_list)
    for index in my_list:
        print("{} это {}".format(index, type(index)))


def task_2():
    counter = 0
    changing_dict = []
    print("Введите элементы массива. Чтобы завершить, напишите 'конец|end'")
    while True:
        changing_dict_save = (input("Введите {}-е значение массива - ".format(counter+1)))
        if changing_dict_save == "конец" or changing_dict_save == "end" or changing_dict_save == "rjytw" or changing_dict_save == "утв":
            print(sort_dict(changing_dict, counter))
            break
        else:
            changing_dict.append(changing_dict_save)
            counter += 1
            continue


def task_3():
    task3_dict = {"зима":(12, 1, 2),"весна":(3, 4, 5),"лето":(6, 7, 8),"осень":(9, 10, 11)}
    task3_list = ["зима", "зима", "весна", "весна", "весна", "лето", "лето", "лето", "осень", "осень", "осень", "зима"]
    choice = input("Каким способом решать задание: через list(1) или dict(2)? - ")
    try:
        month = int(input("Номер месяца: "))
        if choice == "list" or choice == "1":
            print("Месяц под номером {} - {}".format(month, task3_list[month - 1]))
        else:
            for key in task3_dict.keys():
                if month in task3_dict[key]:
                    print("Месяц под номером {} - {}".format(month, key))
    except ValueError:
        print("Надо ввести число!")



def task_4():
    user_string = input("Введите строку:\n")
    user_list_string = user_string.split()
    print(user_list_string)
    for i in range(len(user_list_string)):
        buf = user_list_string[i]
        print("{}) {}".format(i+1, buf[:10]))


def task_5():
    my_list = [7, 5, 3, 3, 2]
    user_num = int(input("Enter your number: "))
    for index in range(len(my_list)):
        if user_num > my_list[index]:
            my_list.insert(index, user_num)
            print(my_list)
            break
        if index == len(my_list)-1:
            my_list.append(user_num)
            print(my_list)


def task_6():
    # не знаю как делать
    return


while True:
    while True:
        try:
            number_of_task = int(input("Введите номер нужного задания: "))
        except ValueError:
            print("Необходимо ввести число, а не строку...")
            continue
        print('---------------------------------------')
        if number_of_task == 1:
            task_1()
            break
        elif number_of_task == 2:
            task_2()
            break
        elif number_of_task == 3:
            task_3()
            break
        elif number_of_task == 4:
            task_4()
            break
        elif number_of_task == 5:
            task_5()
            break
        elif number_of_task == 6:
            task_6()
            break
        else: print('Упс! Такого задания нет...')
    print('---------------------------------------')
    your_choice = input("Посмотрим еще какое-то задание? Да/нет/bool - ")
    if your_choice in yes_dict:
        print('---------------------------------------')
        continue
    else:
        print('Спасибо! На этом все...')
    break
