paint = int(input())
bottlecaps = int(input())
dollars = int(input())

money = paint // bottlecaps * dollars
money += paint % bottlecaps

print(money)