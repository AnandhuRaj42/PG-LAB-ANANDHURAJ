str=input("enter a string:")
if(str.endswith("ing")):
    str+='ly'
else:
    str+='ing'
print("new string is:",str)
