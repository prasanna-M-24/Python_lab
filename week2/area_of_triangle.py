import math

print("finding area of triangle using Heron's formula")
a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))
c = float(input("Enter length of side c: "))
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("The area of the triangle is:", area)

print("finding area of triangle using base and height")
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area_bh = 0.5 * base * height
print("The area of the triangle is:", area_bh)

print("finding area of triangle using angle between two sides")
side1 = float(input("Enter length of side 1: "))
side2 = float(input("Enter length of side 2: ")) 
angle_deg = float(input("Enter the angle between the two sides in degrees: "))  
angle_rad = math.radians(angle_deg)
area_angle = 0.5 * side1 * side2 * math.sin(angle_rad)
print("The area of the triangle is:", area_angle)