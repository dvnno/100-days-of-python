import random
from functools import reduce

fruits = ["lemon", "strawberry", "apple"]

print(fruits[random.randint(0, len(fruits) - 1)])

print(fruits[-1]) # apple
print(fruits[0]) # lemon

capital_fruits = map(lambda fruit: fruit.upper(), fruits)
print(list(capital_fruits))

fruits_with_a = filter(lambda fruit: "a" in fruit, fruits)
print(list(fruits_with_a))

fruits_letter_count = reduce(lambda count, fruit: count + len(fruit), fruits, 0)
print(fruits_letter_count)

friends = ["Alice", "Bob", "Charlie", "Darlene", "Eric"]
print(random.choice(friends))

dirty_fruits = ["Strawberries", "Grapes", "Peaches", "Pears", "Nectarines", "Apples", "Cherries", "Blueberries"]
dirty_vegetables = ["Spinach", "Kale", "Peppers", "Green beans"]
dirty_dozen = [dirty_fruits, dirty_vegetables]

print(random.choice(dirty_dozen[random.randint(0, 1)]))
