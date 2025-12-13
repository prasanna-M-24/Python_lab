p=float(input("Enter the principal amount: "))
t=float(input("Enter the time in years: "))
r=float(input("Enter the rate of interest: "))
amount = p * (1 + r / 100) ** t
ci = amount - p
print("Compound Interest is: ", ci)