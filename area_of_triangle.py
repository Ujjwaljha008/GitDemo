"""
When all the length of sides of the triangle is known - a,b,c
Semi perimeter (s)=(a+b+c)/2
Area=sqrt of (s*(s-a)*(s-b)*(s-c))
"""

a=float(input("Enter first side of triangle: "))
b=float(input("Enter second side of triangle: "))
c=float(input("Enter third side of triangle: "))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area of Triangle with given side is",round(area,2))


