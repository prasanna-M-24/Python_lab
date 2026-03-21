# Step 1: Writing to a file
with open("example.txt", "w") as f:
    f.write("Hello, this is line one.\n")
    f.write("This is line two.\n")
    f.writelines(["Line three\n", "Line four\n"])

# Step 2: Reading from the file
with open("example.txt", "r") as f:
    print("Using read():")
    content = f.read()
    print(content)

# Reset file pointer and read again
with open("example.txt", "r") as f:
    print("Using readline():")
    line1 = f.readline()
    print(line1)
    line2 = f.readline()
    print(line2)

with open("example.txt", "r") as f:
    print("Using readlines():")
    lines = f.readlines()
    print(lines)