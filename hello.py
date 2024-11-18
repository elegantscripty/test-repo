import random

def say_hello(name):
    print(f"Good morning, {name}")

def guess_number(num_range):
    randnum = random.randrange(num_range)
    print(f"I guess {randnum}")

if __name__ == "__main__":
    say_hello("Mary Brown")
    say_hello("Peter Piper") 
    guess_number(20)
    guess_number(10)
    guees_number(6)

