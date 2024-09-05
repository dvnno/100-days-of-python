import math

print(123 + 456)
print(123 - 456)
print(123 * 456)
print(123 / 456)
print(123 // 456) # converts to an integer (floor round)
print(123 % 456)
print(123 ** 456) # exponentiation
print(math.floor(math.sin(3.141592653589793)))

# follows order of operations
print(3 * 3 + 3 / 3 - 3) # 7.0
print(3 * (3 + 3) / 3 - 3) # 3.0

num = 10
num += 10
print(num) # 20

print(f"Num is {num}")