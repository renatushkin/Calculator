def calculator():
    print('Простой калькулятор\n')
    print('Выберите операцию:')
    print('1. Сложение (+)')
    print('2. Вычитание (-)')
    print('3. Умножение (*)')
    print('4. Деление (/)\n')

    choice = input('Введите номер операции (1/2/3/4): ')

    if choice not in ['1', '2', '3', '4']:
        print('Некорректный выбор. Попробуйте снова')
        return

    try:
        num1 = float(input('\nВведите первое число: '))
        num2 = float(input('Введите второе число: '))
    except ValueError:
        print('\nОшибка: нужно вводить число!')
        return

    if choice == '1':
        result = num1 + num2
        print(f"\nРезультат: {num1} + {num2} = {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"\nРезультат: {num1} - {num2} = {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"\nРезультат: {num1} * {num2} = {result}")
    elif choice == '4':
        if num2 == 0:
            print('\nОшибка: делить на ноль нельзя!')
        else:
            result = num1 / num2
            print(f"\nРезультат: {num1} / {num2} = {result}")

calculator()