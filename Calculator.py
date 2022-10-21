
def calculator():
    print('1. substract')
    print('2. add')
    print('3. multiply')
    print('4. divide')

    choose= int(input('pick 1-4 '))
    
    number1 = int(input('number 1: '))
    number2 = int(input('number 2:'))
    
    
    substract = number1 - number2
    add = number1 + number2
    multiply = number1 * number2
    divide = number1 / number2


    if choose == 1:
        print(str(number1) +' - '+ str(number2) + ' = ' + str(substract))
    elif choose == 2:
        print(str(number1) +' + '+ str(number2) + ' = ' + str(add))
    elif choose == 3:
        print(str(number1) +' * '+ str(number2) + ' = ' + str(multiply))
    elif choose == 4:
        print(str(number1) +' / '+ str(number2) + ' = ' + str(divide))

        
stop = True
while stop == True:
    calculator()
    x = input('Do you want to do another one? (yes/no) ')
    if x == 'yes':
        stop = True
    else:
        stop = False
        break