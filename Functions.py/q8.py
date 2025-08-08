# Given a list of numbers [1, 2, 3, 4, 5], use map() and a lambda function to return a new list with
# each number doubled.

l = [1, 2, 3, 4, 5]
double = map(lambda value : 2 * value, l)
print(list(double))