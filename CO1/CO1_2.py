y1=int(input("enter the year1 :"));
y2=int(input("enter the year2 :"));
print("Future leap years:")
for i in range(y1,y2):
       if i%4==0 and i%100!=0:
        print(i)
        
