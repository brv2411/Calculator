#Calculator
print ('''
                                            _________________________________
                                            |                                                                      |
                                            |                   1. Addition                                  |
                                            |                   2. Subtraction                            |
                                            |                   3. Multiplication                          |
                                            |                   4. Division                                   |
                                            |                   5. True/False                              |
                                            |                       a. Addition                              |
                                            |                       b. Subtraction                         |
                                            |                       c. Multiplication                       |
                                            |                       d. Division                                |
                                            |                   6. Exit                                         |
                                            |_________________________________|''')
a = 0
while a != '6':
    a = input('Choose a NUMBER associated with the desired OPERATION ')
    if a == '1':
        print ('Addition')
        b = int(input('Enter a NUMBER '))
        c = int(input('Enter another NUMBER '))
        print (b + c)
    elif a == '2':
        print ('Subtraction')
        b = int(input('Enter a NUMBER '))
        c = int(input('Enter another NUMBER '))
        print (b - c)
    elif a == '3':
        print ('Multiplication')
        b = int(input('Enter a NUMBER '))
        c = int(input('Enter another NUMBER '))
        print (b * c)
    elif a == '4':
        print ('Division')
        b = int(input('Enter a NUMBER '))
        c = int(input('Enter another NUMBER '))
        print (b / c)
    elif a == '5a':
        print ('True/False:Addition')
        b = int(input('Enter a NUMBER '))
        c = int(input('Enter another NUMBER '))
        d = int(input('Enter what you think is the answer '))
        e = (b + c)
        if d == e:
            print ('True')
        else:
            print ('False')
            print (e)
    elif a == '5b':
        print ('True/False:Subtraction')
        b = int(input('Enter a NUMBER '))
        c = int(input('Enter another NUMBER '))
        d = int(input('Enter what you think is the answer '))
        e = (b - c)
        if d == e:
            print ('True')
        else:
            print ('False')
            print (e)
    elif a == '5c':
        print ('True/False:Multiplication')
        b = int(input('Enter a NUMBER '))
        c = int(input('Enter another NUMBER '))
        d = int(input('Enter what you think is the answer '))
        e = (b * c)
        if d == e:
            print ('True')
        else:
            print ('False')
            print (e)
    elif a == '5d':
        print ('True/False:Division')
        b = int(input('Enter a NUMBER '))
        c = int(input('Enter another NUMBER '))
        d = int(input('Enter what you think is the answer '))
        e = (b / c)
        if d == e:
            print ('True')
        else:
            print ('False')
            print (e)
else:
    exit
