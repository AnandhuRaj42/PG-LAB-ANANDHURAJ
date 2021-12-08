import operator
dic={"javascript":2,"java":1,"python":3}
print("Before Sorting",dic);
print("Sorting Ascending")
s1=sorted(dic.items(),key=operator.itemgetter(0))
print(s1)
print("Sorting descending")
s2=sorted(dic.items(),key=operator.itemgetter(0),reverse=True)
print(s2)
