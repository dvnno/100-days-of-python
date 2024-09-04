print("hello"[4])
# o
print("hello"[-4])
# e
# negative indices count from rtl starting at -1

print("123" + "456")
# string concat

print(123 + 456)
# 579

# you can use _ as you would , for large integers (only single _ works)
print(123_456_789)
print(123456789)
print(1_2_3_4_5_6_7_8_9)

# float
print(3.14159)

# Boolean (note the caps)
print(True)
print(False)


def times_three(*args):
    if len(args) > 0 and (type(args[0]) is int or type(args[0]) is float):
        return args[0] * 3
    elif len(args) == 0:
        return "You didn't pass anything"
    else:
        return "That was not a number value you can multiply"


print("4 times 3 is: ", times_three(4))
print("What happens when you give no argument? ", times_three())
print("What happens when you pass in None?", times_three(None))

print(len([1, 2, 3, 4, 5]))

print(type("String"))
print(type(2.1))
print(type(34))
print(type(True))
print(type([1, 2, 3, 4]))
print(type(None))
print(type({"fizz": "buzz"}))

print(int("123") + 456)
# 579

print(str(123) + str(456))
#"123456"

# A conversion method for each primitive
# int()
# float()
# str()
# bool()

print(int(99.9))

print("Number of letters in your name: " + str(len(input("What is your name?\n"))))