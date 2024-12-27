from random import randrange

print('Welcome to Guessing Game')
print('----------------------------------')
print('The rules are simple: I think of a number from 1 to 100, and you try to guess it.')
print("Ready? Let's go!")
print('*makes strange sounds*')
num = randrange(1, 101)
print('So, the number is guessed, try to guess it.')
while True:
    print('Enter the number: ', end='')
    x = input()
    if x.isdigit() and 0 < int(x) < 101:
        x = int(x)
        if x > num:
            print('The guessed number is smaller. Try again.')
        elif x < num:
            print('The guessed number is higher. Try again.')
        else:
            print(f'Congratulations! You guessed the number {num}!')
            break
    else:
        print('You must enter an integer between 1 and 100. Try again.')
