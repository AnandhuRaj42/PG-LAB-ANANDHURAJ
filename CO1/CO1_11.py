
x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
z = int(input("Enter 3rd number: "))
large=x
if (large<y) and (y>z):
    large = y
elif (large< z) and (y <z):
    large = z
print("The largest number is",large)
