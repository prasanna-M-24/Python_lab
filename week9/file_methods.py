# Step 1: Write data into a file
with open("demo.txt", "w") as f:
    f.write("First line\n")
    f.write("Second line\n")
    f.write("Third line\n")
    f.flush()   # flush ensures immediate write

# Step 2: Read with seek() and tell()
# Open in binary mode to allow whence=1
with open("demo.txt", "rb") as f:
    print("Initial position:", f.tell())   # 0 at start
    
    # Move pointer to 6th byte from beginning
    f.seek(6, 0)
    print("After seek(6,0):", f.tell())
    print("Read from here:", f.readline())
    
    # Move pointer 5 bytes forward from current position
    f.seek(5, 1)
    print("After seek(5,1):", f.tell())
    print("Read from here:", f.readline())
    
    # Move pointer 0 bytes from end (whence=2)
    f.seek(0, 2)
    print("After seek(0,2):", f.tell())