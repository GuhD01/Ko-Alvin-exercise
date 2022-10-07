time = eval(input('Enter the number of seconds: '))
hours = (time // 3600)
minute = ((time % 3600) // 60)
seconds = (time % 3600) % 60
print(f'result: {hours}:{minute}:{seconds}')