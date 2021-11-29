str1="hello"
str2="world"
a=str1[0]
b=str2[0]
str2=b+str1[1:]+" "+ a+str2[1:]
print(str2)
