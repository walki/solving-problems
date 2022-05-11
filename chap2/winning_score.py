a3 = int(input())
a2 = int(input())
a1 = int(input())
b3 = int(input())
b2 = int(input())
b1 = int(input())

a_score = a3 * 3 + a2 * 2 + a1
b_score = b3 * 3 + b2 * 2 + b1

if a_score > b_score:
    print('A')
elif b_score > a_score:
    print('B')
else:
    print('T')