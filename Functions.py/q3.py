# Create a function power(base, exponent=2) that returns the result of base raised to the power of
# exponent.Demonstrate it with and without the exponent argument.


def power(base, exponent = 2):
    return base ** exponent

print(power(2,3)) #with arguments

print(power(3)) #without arguments which uses default exponent as 2

