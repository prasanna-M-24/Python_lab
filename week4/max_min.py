num=list(map(int,input("Enter three numbers to find the largest and the smallest: ").split()))
maximum=minimum=num[0]
for i in num:
    if i>maximum:
        maximum=i
    else: 
        minimum=i
print("Maximum number in the list: ",maximum,"\n Minimum number in the list: ", minimum)

