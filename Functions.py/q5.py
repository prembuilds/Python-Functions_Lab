# Create a function sum_numbers(*args) that accepts any number of numeric arguments and returns
# their sum.Test it with 2, 3, and 5 numbers.

def sum_numbers(*elements):
    res = 0
    for value in elements:
        res += value
    return res

print(sum_numbers(2,3))
print(sum_numbers(2,3,4))
print(sum_numbers(2,3,4,5))
print(sum_numbers(3,4,5,6,7,8))