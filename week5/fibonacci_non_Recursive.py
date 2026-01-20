n = int(input("Enter a number: "))
first = 0
second = 1
print("Fibonacci Series: ")
for i in range(1,n+1):
    print(first,end = " ")
    next = first + second
    first = second
    second = next