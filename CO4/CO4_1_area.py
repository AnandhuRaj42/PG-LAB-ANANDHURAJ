class rectangle:
    def __init__(self,le,br):
        self.le=le
        self.br=br
    def area(self):
        ar=self.le*self.br
        return(ar)
       
    def perimeter(self):
        pr=2*(self.le+self.br)
        return(pr)
       
print("First rectangle")
l1=int(input("Enter the length :"))
b1=int(input("Enter the breadth :"))
p1=rectangle(l1,b1)
print("Area=",p1.area())
print("Perimeter=",p1.perimeter())
print("---------------------")
print("Second rectangle")
l2=int(input("Enter the length :"))
b2=int(input("Enter the breadth :"))
p2=rectangle(l2,b2)
print("Area=",p2.area())
print("Perimeter=",p2.perimeter())
if(p1.area()>p2.area()):
    print("Rectangle 1 area is large")
else:
    print("Rectangle 2 area is large")








        
