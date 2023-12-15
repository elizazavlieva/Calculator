def addition(num, num1):
    return num + num1


def subtraction(num, num1):
    return num - num1


def multiplication(num, num1):
    return num * num1


def division(num, num1):
    return num / num1


def solution(choice,num, num1):
    if choice == 1:
        result = addition(num, num1)
        print(f'Result: {num} + {num1} = {result}')
    elif choice == 2:
        result = subtraction(num, num1)
        print(f'Result: {num} - {num1} = {result}')
    elif choice == 3:
        result = multiplication(num, num1)
        print(f'Result: {num} * {num1} = {result}')
    elif choice == 4:
        if num % num1 == 0:
            result = int(division(num, num1))
            print(f'Result: {num} / {num1} = {result}')
        else:
            result = division(num, num1)
            print(f'Result: {num} / {num1} = {result:.2f}')


def main():
    print('Menu:\n \n'
          '1.Addition\n'
          '2.Subtraction\n'
          '3.Multiplication\n'
          '4.Division\n'
          '5.Quit')
    while True:
        user_choice = int(input('Enter your choice (1/2/3/4/5): '))
        if user_choice > 5:
            while user_choice > 5:
                print('Please enter valid operation!')
                user_choice = int(input('Enter your choice (1/2/3/4/5): '))
        if user_choice == 5:
            print('Goodbye!')
            break
        first_num = int(input('Enter the first number: '))
        second_num = int(input('Enter the second number: '))
        if second_num == 0 and user_choice == 4:
            print('The operation cannot be performed! Please enter a number greater than 0!')
            second_num = int(input('Enter the second number: '))

        solution(user_choice, first_num, second_num)


main()
