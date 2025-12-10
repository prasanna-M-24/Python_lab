import math

#Area of circle calculation
r=int(input("Enter the radius of the circle: "))
print("area of the circle with radius ",r," is: ", math.pi*r**2)

#pythagora's theorem
s1=int(input("Enter length of the first side:" ))
s2=int(input("Enter the length of the second side: "))
s3=math.sqrt(((s1)**2)+((s2)**2))
print("the length of the third side is: ", s3)

#find the x co-ordinate at the angle 90 degrees
r=int(input("Enter the radius to locate point on x-axis: "))
print("x co-ordinate is: ",r*math.cos(math.radians(90)))

#to find the position of the pendullum exactly
a=float(input("Enter the amplitude: "))
l=float(input("Enter the length of the pendullum: "))
t=float(input("Enter time: "))
y=a*(math.sin((math.sqrt(9.8/l))*t))
print("pendullum side ways position at time ",t,"is: ",y)