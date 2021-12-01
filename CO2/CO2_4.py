from math import sqrt as s
print("Numbers are:")
for i in range(999,10000):
    if s(i)==int(s(i)) and i%2==0:
        print(i,end=" ")
