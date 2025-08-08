# Given a list of temperatures in Celsius [36.5, 37.0, 39.2, 35.6, 38.7],convert them to Fahrenheit
# using map(),Filter out those above 100°F using filter().

temp_celsius = [36.5, 37.0, 39.2, 35.6, 38.7]
temp_fahrenheit = map(lambda temp: temp * (9/5) + 32, temp_celsius)
result = filter(lambda value : value > 100, temp_fahrenheit)
print(list(result))
