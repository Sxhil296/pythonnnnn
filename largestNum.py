# a = 12
# b = 14
# c = 6
#
# if (a > b) and (b > c):
#     print('{a} is the largest.')
# elif (b > a) and (a > c):
#     print(f'{b} is the largest.')
# else:
#     print(f'{c} is the largest.')


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if (num1 > num2) and (num2 > num3):
    print(f'{num1} is the largest number.')
elif (num2 > num1) and (num1 > num3):
    print(f'{num2} is the largest.')
else:
    print(f'{num3} is the largest.')