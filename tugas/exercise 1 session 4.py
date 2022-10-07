bill = int(input('Enter amount of bill: '))
people = int(input('Enter the number of people: '))
tips =  int(input('Enter the amount of tips (%): '))

Tip_amount = bill * tips/100
bill_person = bill/people
total = bill_person + Tip_amount
print('The total tip is: $','{:.2f}'.format(Tip_amount))
print('The total bill is: $','{:.2f}'.format(total))