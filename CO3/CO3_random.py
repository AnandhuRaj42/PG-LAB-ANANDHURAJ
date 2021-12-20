import random

print("seed:",random.seed(10))
print("random float:",random.random())

mylist = ["apple", "banana", "cherry"]

print("sample:",random.sample(mylist, k=2))

print(random.random())

mylist2 = ["apple", "banana", "cherry"]
random.shuffle(mylist2)
print("shuffle:",mylist2)



mylist3 = ["apple", "banana", "cherry"]

print("choice:",random.choice(mylist3))
