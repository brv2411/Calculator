#This is my calculator. We will be using multi-line statements, print, input, variables, exit and if, else and elif statements
#The aim of this project is to help learning Python programmers programme a basic calculator, so remember nothing too fancy
print ("Calculator")
print (""" _____________________________
|                            |
|    1. Addition             |
|    2. Subtraction          |
|    3. Multiplication       |
|    4. Division             |
|    5. Exit                 |
|____________________________|
""")
z = 4
z = int(z)
while int(z) < 5:
    z = input("Choose an operation by typing a NUMBER")
    x = input("1st Number")
    x = int(x)
    y = input("2nd Number")
    y = int(y)
    if z == 1:
        print (x + y)
    elif z == 2:
        print (x - y)
    elif z == 3:
        print (x * y)
    elif z == 4:
        print (x / y)
else:
    exit
