n = int(input("Enter a number: "))
def primeNum(num, div=2):
    if num < 2:
        return False
    if div > num**0.5:
        return True
    if num % div == 0:
        return False
    return primeNum(num, div + 1)
if primeNum(n):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")