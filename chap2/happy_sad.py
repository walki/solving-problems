line = input()

happy = line.count(':-)')
sad = line.count(':-(')

if happy == 0  and sad == 0:
    print('none')
elif happy > sad:
    print('happy')
elif sad > happy:
    print('sad')
else:
    print('unsure')
