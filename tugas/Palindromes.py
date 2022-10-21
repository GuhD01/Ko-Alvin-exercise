# a program to show if a number or string is a palindrome or not


word = str(input('input a word/number: '))
x = ''
for i in word:
    x = i + x
    print(x)
if x == word:
    print("palindrome")
else:
    print('it is not')
        