print(True and False) # False
print(True or False) # True
print(not True) # False
print(not False) # True
a = 10
print(15 > a and a > 5) # True
print(15 > a or a > 5) # True
print(not a) # False
print(not not a) # True
print(not 15 > a) # False

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("That'll be $5")
    elif age <= 18:
        print("That'll be $7")
    elif 45 <= age and age <= 55:
        print("You get to ride for free!")
    else:
        print("That'll be $12")
else:
    print("Sorry you have to grow taller before you can ride")

