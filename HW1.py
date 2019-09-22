#Calculator
def calculator (x,s,y): #Create function with 3 arguments
    d={'+','-','*','/'}
    if s not in d:
        a = "Mistake action"#Remove all action that function can`t do
    else:
        if s == '+':
             a = x+y
        if s == '-':
            a = x-y
        if s == '*':
            a = x*y
        if s == '/':
            if y == 0:
                a = "You can`t divide on zero"
            else:
                a = x/y
    return print(a)#get a result
x =int(input()) #this part can also be in function
s =input()# Но я не понимаю как сделать чтобы функция запрашивала данные с клавиатуры, а не вводить их в скобках
y =int(input())
calculator(x,s,y)