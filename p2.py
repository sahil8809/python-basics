# Basic Python program for learning operators and simple logic

# 1. Add two numbers
try:
    num1 = float(input("Enter first number: "))
except EOFError:
    num1 = 10.0

try:
    num2 = float(input("Enter second number: "))
except EOFError:
    num2 = 5.0

print(f"The sum of {num1} and {num2} is: {num1 + num2}")

# 2. Floor division and modulus examples
print("\nFloor division and modulus examples:")
print(f"-10 // 3 = {-10 // 3}")
print(f"-10 % 3 = {-10 % 3}")
print(f"-10 % 2 = {-10 % 2}")
print(f"-10 // 2 = {-10 // 2}")
print(f"10 * 2 = {10 * 2}")
print(f"10 ** 2 = {10 ** 2}")

# 3. Comparison operators
print("\nComparison operators:")
print(f"5 == 5 -> {5 == 5}")
print(f"5 != 3 -> {5 != 3}")
print(f"3 < 5 -> {3 < 5}")
print(f"5 <= 5 -> {5 <= 5}")
print(f"8 > 5 -> {8 > 5}")
print(f"8 >= 8 -> {8 >= 8}")

# 4. Find the greatest value
x = 500
y = 40
z = 80

numbers = {"x": x, "y": y, "z": z}
greatest_key = max(numbers, key=numbers.get)
print(f"\nThe greatest value is {numbers[greatest_key]} from {greatest_key}")

# 5. Logical operators
print("\nLogical operator example:")
print(f"(x > y) and (z < x) -> {(x > y) and (z < x)}")
print(f"(x < y) or (z > y) -> {(x < y) or (z > y)}")
print(f"not (x == 500) -> {not (x == 500)}")