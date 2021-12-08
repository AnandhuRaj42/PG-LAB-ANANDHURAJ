def fact(a):
    print("Factors of",a,"is")
    for i in range(1,a+1):
        if(a%i==0):
            print(i)
n=int(input("Enter the Number "))
fact(n)
            
            
