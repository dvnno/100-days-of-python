if True:
    print("This will always happen.")
elif True & False:
    print("This will never happen.")
else:
    print("This will never happen.")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride")

print(True and False)
print(not True)
print(True & False)
print((not True) or (True and False))
print(True | False)
print(True or False)
print(not True and not False)
print(not True or False)

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("That'll be $5")
    elif 12 <= age <= 18:
        print("That'll be $7")
    else:
        print("That'll be $12")
else:
    print("Sorry you have to grow taller before you can ride")

