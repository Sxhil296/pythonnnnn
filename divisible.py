div = int(input("enter the number: "))
divider = int(input("enter the divider: "))
if div % divider == 0:
    print(f'{div} is divisible by {divider}.')
else:
    print(f'{div} is not divisible by {divider}.')