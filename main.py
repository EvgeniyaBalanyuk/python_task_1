if __name__ == '__main__':

# TASK 1
    # Задание «Площадь и периметр квадрата»
    # Условие задачи
    # Посчитайте площадь и периметр квадрата, сторона которого равна 6.
    a = 6
    perimeter = a * 4
    area = a * a
    print("Периметр:", perimeter)
    print("Площадь:", area)

#TASK2
    # Посчитайте площадь и периметр прямоугольника 5×7
    a = 5
    b = 7
    perimeter = (a + b) * 2
    area = a * b
    print('Периметр:', perimeter)
    print('Площадь:', area)

#TASK3
    # Создайте код, который можно использовать для планирования личных финансов.
    # Сколько денег тратит пользователь на ипотеку в год и сколько он накопит за год (остаток от заработанной платы после оплаты ипотеки и расходов на жизнь), если:
    # заработная плата в месяц = 100 000 руб.,
    # расходы на ипотеку = 30%,
    # расходы на жизнь = 50%
    salary = 100000
    present_mortgage = 30
    present_life = 50
    mortgage = int(salary / 100 * present_mortgage * 12)
    result = int((salary * 12) - ((salary / 100 * present_mortgage * 12) + (salary / 100 * present_life * 12)))
    print("На ипотеку было потрачено", mortgage, "рублей")
    print("Было накоплено", result, "рублей")

#TASK4
    # Создайте код, который можно использовать для планирования личных финансов.
    # Данные вводит пользователь
    salary = int(input("Введите заработную плату в месяц: "))
    mortgage_interest = int(input("Введите, какой процент(%) уходит на ипотеку: "))
    live_interest = int(input("Введите, какой процент(%) уходит на жизнь: "))

    result_mortgage = int(salary / 100 * mortgage_interest * 12)
    accumulated = int((salary * 12) - ((salary / 100 * mortgage_interest * 12) + (salary/100 * live_interest * 12)))
    print(f"На ипотеку было потрачено: { result_mortgage } рублей")
    print(f"Было накоплено: { accumulated } рублей")