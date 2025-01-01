n = int(input('Enter an integer: '))
original = n  # keep the original value
res = 0
while n:
    res *= 10  # increase the digit capacity(разрядность) of the new number before adding the next digit
    res += n % 10  # take the last digit from the given number
    n = n // 10  # cut off the last digit from the given number
print('The number is a palindrome.' if res == original else 'The number is not a palindrome.')
