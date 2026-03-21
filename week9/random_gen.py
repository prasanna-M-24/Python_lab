import random
numbers = [random.randint(1, 100) for _ in range(20)]

with open("random_numbers.txt", "w") as f:
    for num in numbers:
        f.write(str(num) + "\n")
    f.flush()

print("20 random numbers written to random_numbers.txt")