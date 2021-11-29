l1=[1,3,5,7,9,11,34]
l2=[5,13,45,7,20,65]
s=int(0) 
c=int(0)

if len(l1)==len(l2):
  print("same length") 
else:
  print("different length")

for i in range(0,len(l1)):
  s=s+l1[i]
for i in range(0,len(l2)):
  c=c+l1[i]
if(s==c):
  print("equal sum")
else:
  print("not same sum")

print("Same elements are:") 
l=[]
for i in range(0,len(l1)):
  for j in range(0,len(l2)):
    if l1[i]==l2[j]:
        l.append(l1[i] and l2[j]) 
    else:
      continue
print(l)
