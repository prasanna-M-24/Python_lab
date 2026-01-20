n = int(input("Enter a number(Greater than 0): "))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(f"Factorial of {n} is {fact}")