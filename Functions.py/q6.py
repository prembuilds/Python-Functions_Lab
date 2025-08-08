# Write a function student_profile(**kwargs) that prints the key-value pairs passed (e.g., name, age,
# grade). Call it with at least three named arguments.

def student_profile(**details):
    for key, value in details.items():
        print(f"{key} : {value}")

student_profile(name = "Rohan", age = 15, grade = 3.67)
print()
student_profile(name="Ramesh", grade= 4, age = 18)