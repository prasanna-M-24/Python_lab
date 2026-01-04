start=list(map(int,input("Enter range to find no. of even and odd numbers: ").split()))
Even_count=0;odd_count=0
for i in range (start[0],start[1]+1) :
    if i%2==0:
        Even_count+=1
    else:
        odd_count+=1
print("No.of even numbers: ",Even_count)
print("No.of odd numbers: ",odd_count)