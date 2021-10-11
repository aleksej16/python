my_dict = ['yes', 'Yes', 'да', 'Да', 'нуы', 'Нуы', 'lf', 'Lf', '1']


def task_1():
    a = 1
    b = 3
    print(a, 'и', b)
    user_str_first = input("Введите первую строку - ")
    user_str_second = input("Введите вторую строку - ")
    user_number_first = int(input("Введите первое число = "))
    user_number_second = int(input("Введите первое число = "))
    print('Вы ввели числа: {} и {}'.format(user_number_first, user_number_second))
    print('Вы написали следующий текст: {} и {}'.format(user_str_first, user_str_second))


def task_2():
    user_time = int(input('Введите время в секундах: '))
    current_number = user_time
    seconds = 0
    minute = 0
    hour = 0
    while current_number > 0:
        current_number = current_number - 1
        seconds += 1
        if seconds == 60:
            minute += 1
            seconds = 0
        if minute == 60:
            hour += 1
            minute = 0
    print('Итак, ваше время после перевода: {}ч:{}м:{}с'.format(hour, minute, seconds))


def task_3():
    user_number = input('Введите число: ')
    print("{} + {} + {} = {}".format(user_number, user_number + user_number, user_number + user_number + user_number, int(user_number) + int(user_number + user_number) + int(user_number + user_number + user_number)))


def task_4():
    user_number_str = input("Введите целое положительное число: ")
    user_current_digit = 0
    max_digit = 0
    for digit in user_number_str:
        user_current_digit = int(digit)
        if user_current_digit > max_digit:
            max_digit = user_current_digit
    print("Самая большая цифра в числе {} - {}".format(user_number_str, max_digit))


def task_5():
    proceeds = int(input("Выручка = "))
    costs = int(input("Издержки = "))
    number_of_workers = int(input("Введите число сотрудников фирмы = "))
    if proceeds > costs:
        print("Ваша фирма получила прибыль. Рентабельность составила = {}%. Прибыль фирмы в расчете на одного сотрудника = {}".format(((proceeds-costs)/proceeds)*100, (proceeds-costs)/number_of_workers))
    else: print("Ваша фирма убыточна.")


def task_6():
    day = 1
    a = int(input("Сегодня пробежал = "))
    difference = 0
    last_a = 2
    b = int(input("Результат, которого нужно достичь = "))
    while True:
        if a >= b:
            print("И на {}-й день вы достигнете рез-та, пробежав {}км (+{})".format(day, round(a, 2), round(difference, 2)))
            break
        else:
            print("{}-й день: {}км (+{})".format(day, round(a, 2), round(difference, 2)))
            day += 1
            last_a = a
            a = a * 1.1
            difference = a - last_a


while True:
    while True:
        number_of_task = int(input("Введите номер нужного задания: "))
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
    your_choice = input("Посмотрим еще какое-то задание? Да/нет - ")
    if your_choice in my_dict:
        print('---------------------------------------')
        continue
    else:
        print('Спасибо! На этом все...')
    break
