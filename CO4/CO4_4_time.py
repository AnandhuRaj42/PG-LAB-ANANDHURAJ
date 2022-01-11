class time:
    def __init__(self,hr,mt,sec):
        self.__hr=hr
        self.__mt=mt
        self.__sec=sec
    def __add__(self,a):
        h=self.__hr+a.__hr
        m=self.__mt+a.__mt
        if(m>60):
            q=int(m/60)
            r=m%60
            h=h+q
            m=r
        s=self.__sec+a.__sec
        if(s>60):
            q1=int(s/60)
            r1=s%60
            m=m+q1
            s=r1
        print("Added Time is:")
        print(h,":",m,":",s)

print("Time 1")
h1=int(input("Enter Hour: "))
m1=int(input("Enter Minute: "))
s1=int(input("Enter Second: "))
tm1=time(h1,m1,s1)
print("Time 2")
h2=int(input("Enter Hour: "))
m2=int(input("Enter Minute: "))
s2=int(input("Enter Second: "))
tm2=time(h2,m2,s2)
tm1+tm2
