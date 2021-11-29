print("a:\n")
list1=[]
l=[2,-2,45,65,-64,32,-111]
print("positive numbers are  :")
for i in range(len(l)):
    if(l[i]>0):
        list1.append(l[i])
print(list1)
        
print("\nb:\n")
n=int(input("enter the limit\n"))
s=[ i**2 for i in range(1,n+1)]
print(s)
print("\nc:\n")
word =str(input("Enter the word :"))
print("The vowels in the word is: ",end="")
for i in word:
   if i in 'aeiouAEIOU':
      print([i],end=" ")
print("\nd:\n")
w=input("Enter a word:")
print("Ordinal values for each elements:")
for i in w:
    print(i,end=":")
    print(ord(i),end=" ")




    


