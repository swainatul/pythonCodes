num1 = int(input("Enter the hour glass size: "))
for x in range(num1, -1, -2):
    if num1 % 2 != 0 and x > 0:
        print(' '*((num1-x)//2)+'x'*x+' '*((num1-x)//2))
    elif num1 % 2 == 0 and x > 0:
        print(' ' * ((num1 - x) // 2) + 'x' * x + ' ' * ((num1 - x) // 2))
    elif x==0:
        print(' ' * ((num1 // 2) - 1) + 'x' + ' ' * ((num1 // 2) - 1))

for x in range(-1, num1, 2):
    if num1 % 2 != 0 and x > 0:
        print(' '*((num1-x)//2)+'x'*x+' '*((num1-x)//2))
    elif num1 % 2 == 0 and x > 0:
        print(' ' * ((num1 - x) // 2) + 'x' * x + ' ' * ((num1 - x) // 2))
    elif x==0:
        print(' ' * ((num1 // 2) - 1) + 'x' + ' ' * ((num1 // 2) - 1))


