a=[]
n=int(input("Enter the number of elements in list:"))
for x in range(0,n):
    s=input("Enter element"+ str(x+1))
    a.append(s)
    m=len(a[0])
    t=a[0]
for i in a:
    if(len(i)>m):
        m=len(i)
        t=i
print("Longest Word is:",t)
print("Length of longest word is:",m) 
