a = int(input('what is the length of AB? '))
b = int(input("what is the length of BC? "))
c = int(input("what is the length of AC? "))
perimeter = a+b+c
if a+b > c and b + c > a and c + a > b:
    print(perimeter)
else:
    print('input is invalid')