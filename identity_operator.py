x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)      # True
print(y is x)
print(x is z)      # False
print(x is not z)  # True

# x = [1, 2, 3]
# z = [1, 2, 3]

print(x == z)  # True → values same
print(x is z)  # False → objects different