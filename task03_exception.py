# Runtime Exception Examples

# NameError
student_name = "GIS Student"
print(student_name)

# TypeError
result = "GIS" + str(10)
print(result)

# ValueError
number = int("123")
print(number)

# ZeroDivisionError
result = 10 / 2
print(result)

# FileNotFoundError
try:
    with open("missing.txt", "r") as file:
        print(file.read())
except FileNotFoundError as error:
    print("File error:", error)