rect=lambda l,b:l*b
sq=lambda s:s*s
tri=lambda a,b:1/2*a*b
l,b=int(input("Enter the length and breadth of rectangle")),int(input())
print("Area of rectangle is :",rect(l,b))
s=int(input("Enter the side of square"))
print("Area of square is :",sq(s))
l,h=int(input("Enter the breadth and height of triangle")),int(input())
print("Area of triangle is :",tri(l,h))
