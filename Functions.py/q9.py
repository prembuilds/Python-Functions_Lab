# Given a list [10, 15, 20, 25, 30], use filter() and a lambda function to extract numbers divisible by
# 10.

l = [10, 15, 20, 25, 30]
result = filter(lambda x : x % 10 == 0, l)
print(list(result))