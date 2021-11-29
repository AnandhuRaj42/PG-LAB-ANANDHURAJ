s= input("Enter a string : ")
word = s.split()
count= []
for w in word:
    count.append(word.count(w))
print("count of the occurrence:" + str(list(zip(word, count))))
