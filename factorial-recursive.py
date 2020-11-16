def factorial(number):
    """
    get a factorial in recursive function way
    """

    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)

print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(0))
print(factorial(-3))