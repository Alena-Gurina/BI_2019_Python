def calc():
    while 0 == 0:
        print("If you would like to exit press N")
        exit_from_fun = input()
        if exit_from_fun == "N":
            break
        else:
            print("enter an integer, command (+,-,* or /) and 2nd integer")
            x = int(input())
            command = input()
            y = int(input())
            l_of_command = ['+', '-', '*', '/']
            if command not in l_of_command:
                print("Mistake action")
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
