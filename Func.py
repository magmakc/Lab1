import random

def random_number(a, b):
    b = random.randint(b, 100)
    a = random.randint(a, 100)
    print(f"a = {a}\nb = {b}\nSummary = {a+b}")
