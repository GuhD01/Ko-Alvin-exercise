prime = int(input('Enter a number: '))

for i in range(2,prime-1):
    if prime % i == 0:
        print('it is a prime')
        break
else:
    print('it is not a prime')






# number = eval(input('Enter a number: '))
# if number % 2 == 0 or number % 3 == 0 or number % 4 == 0 or number % 5 == 0:
#     print('it is not prime number')
# else:
#     print('it is a prime number ')