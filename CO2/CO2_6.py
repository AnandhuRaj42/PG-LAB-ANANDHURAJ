str1=str(input("Enter the string : "))
fq= {}
for i in str1:
    if i in fq:
        fq[i] += 1
    else:
        fq[i] = 1
print ("Count of all characters : ",fq)
