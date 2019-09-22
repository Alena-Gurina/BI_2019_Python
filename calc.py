def calc() -> object:
    while 0 == 0:
        print('If you would like to exit press N')  # Would you like to continue?
        exit_from_fun = input()
        if exit_from_fun == "N":
            break
        else:
            print('enter an integer, command (+, -, * or /) and 2nd integer')
            x = int(input())
            command = input()
            y = int(input())
            l_of_command = ['+', '-', '*', '/']
            if command not in l_of_command:
                print('Mistake action, command could be only +, -, * or /')
                # what command could do this function
                continue
            else:
                result = None
                if command == '+':
                    result = x + y
                if command == '-':
                    result = x - y
                if command == '*':
                    result = x * y
                if command == '/':
                    if y == 0:
                        result = "You can`t divide on zero"
                    else:
                        result = x / y
                print(result)
                continue
    return


calc()
