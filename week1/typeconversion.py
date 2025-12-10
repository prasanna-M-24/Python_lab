s = input("Enter a string (numerical): ")
ch = input("Enter a single char: ")
s2 = input("Enter a string (non-numerical): ")

num = int(input("Enter a num: "))
num2 = float(input("Enter a floating point number: "))

print("Entered:", s, "type:", type(s))
print("Entered:", ch, "type:", type(ch))
print("Entered:", s2, "type:", type(s2))
print("Entered:", num, "type:", type(num))
print("Entered:", num2, "type:", type(num2))

# typecasting string → int
print("after typecasting:", s, "type:", type(s), "→", type(int(s)))

# ASCII value
print("ASCII value of", ch, "is", ord(ch))

# int → float
print("after typecasting (int to float):", num, "→", float(num), "type:", type(float(num)))

# int → str
print("after typecasting (int to str):", num, "→", str(num), "type:", type(str(num)))

# float → int
print("after typecasting (float to int):", num2, "→", int(num2), "type:", type(int(num2)))

# float → str
print("after typecasting (float to str):", num2, "→", str(num2), "type:", type(str(num2)))
