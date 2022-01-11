class rect:
    def __init__(self,l,b):
        self.__l=l
        self.__b=b       
    def __lt__(self,a):
        a1=self.__l*self.__b
        a2=a.__l*a.__b
        if(a1<a2):
            return(True)
print("recatngle1")
l1=int(input("Enter the length"))
b1=int(input("Enter the breadth"))
print("recatngle2")
l2=int(input("Enter the length"))
b2=int(input("Enter the breadth"))
ar1=rect(l1,b1)
ar2=rect(l2,b2)
if(ar1<ar2):
    print("rect1 area less")
else:
    print("rect2 area less")




