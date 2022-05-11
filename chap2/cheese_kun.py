w = int(input())
c = int(input())

reaction = ''

if w == 3 and c >= 95:
    reaction = 'absolutely'
elif w == 1 and c <= 50:
    reaction = 'fairly'
else:
    reaction = 'very'

print('C.C. is ' + reaction + ' satisfied with her pizza.')