# Basic Mathematical Operations: 8 KYU

# Your task is to create a function that does four basic mathematical operations.

# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.

def basic_op(operation, value1, value2):
    if operation == "+": return value1 + value2
    if operation == "-": return value1 - value2
    if operation == "*": return value1 * value2
    if operation == "/": return value1 / value2


print(basic_op('+', 4, 7)) # 11
print(basic_op('-', 15, 18)) # -3
print(basic_op('*', 5, 5)) # 25
print(basic_op('/', 49, 7)) # 7
