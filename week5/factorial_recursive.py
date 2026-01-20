n = int(input("Enter a number(Greater than 0): "))
def fact(n):
    if(n == 0 or n==1):
        return 1
    else:
        return n * fact(n-1)

print(f"Factorial of {n} is {fact(n)}")