"""
| Operator | Meaning                |
| -------- | ---------------------- |
| `in`     | Value present hai      |
| `not in` | Value present nahi hai |

"""


name = 'sahil'
print('a' in name)  # True
print('s' in name)  # True
print('k' in name)  # False 

fruits = ["apple","mango","orange","banana","guava"]
if "banana" in fruits:
    print("YES banana is present!")
print("litchi" not in fruits) # true
print("litchi" in fruits) # False

## NOTE -> in dictionaries memborship operator checks only keys not values

salary = {
    "sahil" : 40000,
    "Tony Stark" : 50000,
    "Elon"  : 20000,
    "MODI PAGLU" : 10,
    500 : "Thor"
}
print("Tony Stark" in salary) # true
print("sahil" in salary) # true
print(10 in salary) # False
print(500 in salary) # true


"""
Logical    →  and, or, not
Assignment →  =, +=, -=, *=, /=, //=, %=, **= ...
Identity   →  is, is not
Membership →  in, not in
"""