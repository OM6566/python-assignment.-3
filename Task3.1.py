a = int(input('Enter a number: '))

def factorial(n):
    if n < 2:
        return n
    else:
        return n * factorial(n - 1)

print('The factorial of', a, 'is: ', factorial(a))