height = float(input("Please enter your height in m:\n"))
weight = float(input("Please enter your weight in kg:\n"))

# Write your code here.
# Calculate the bmi using weight and height.
bmi = round(weight / (height ** 2), 2)

print("Your BMI is ", bmi)
