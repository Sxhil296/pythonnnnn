def find_factors(x):
    print(f'The factors of {x} are: ')
    for i in range(1, x+1):
        if x % i == 0:
            print(i, sep=', ')

            #print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

number = int(input("Enter the number: "))
find_factors(number)