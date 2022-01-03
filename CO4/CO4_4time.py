class time:
    def __init__(self,hr,mt,sec):
        self.__hr=hr
        self.__mt=mt
        self.__sec=sec
    def __add__(self,a):
        h=self.__hr+a.__hr
        m=self.__mt+a.__mt
        s=self.__sec+a.__sec
        print(h,":",m,":",s)

print("Time 1")
h1=int(input("enter hour"))
m1=int(input("enter minute"))
s1=int(input("enter Second"))
tm1=time(h1,m1,s1)
print("Time 2")
h2=int(input("enter hour"))
m2=int(input("enter minute"))
s2=int(input("enter Second"))
tm2=time(h2,m2,s2)
tm1+tm2


