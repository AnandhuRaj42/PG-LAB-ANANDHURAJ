n=int(input("enter the limit\n"));
print("The pattern is:");
for i in range(n):
    for j in range(1,i+2):
        print(j,end="")
    print()
