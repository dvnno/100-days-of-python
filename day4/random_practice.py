import random
import my_module

print(random.randint(1, 10))
print(my_module.favorite_number)

print(random.random())
print(random.random() * 10)
print(int(random.random() * 10) + 1) # Equivalent to line 4
print(random.uniform(1, 10)) # float

coin = random.choice(["Heads", "Tails"])
print(coin)

def print_coin(coin):
    if coin == 0:
        print("Heads")
    elif coin == 1:
        print("Tails")
    else:
        print("Something terrible has happened. Perhaps your computer was hit by a cosmic ray?")

coin = random.randint(0, 1)
print_coin(coin)

coin = round(random.random())
print_coin(coin)
