lt=[]
n1=int(input("Enter a limit:"))
print("Enter values")
for i in range(0,n1):
    lt.append(int(input()))
print("\nThe list is:\n")
for i in range(0,len(lt)):
  if lt[i]>=100:
      print("over") 
  else:
      print(lt[i]) 
