# print("Twinkle Twinkle little star")
# print("what you wonder what you are")

# from playsound import playsound
# playsound("f:\\python\\play.mp3")

# import os
# print(os.listdir())

# a = "tanisha"
# b = 25
# c = 53.54

# print(a,b,c)

# print(type(a))
# print(type(b))
# print(type(c))

# print("the value of b+c : ", b+c)

# a = 9
# print("remainder when a divivded by 2 is: ", a%2)

# a = int(input("Enter first no. : "))
# b = int(input("Enter second no. : "))

# c = (a+b)/2
# d = a*a
# print("the average value of ",a, " and ",b, " is : ",c)

# print("The square of ",a, " is : ", d)

# name = "tanisha's"

# print(name)
# print(type(name))
# print(name[-5])

# greet = "Good Morning"

# name = str(input("Enter your name: "))

# print(greet + " " + name)     #concatenation

# print(greet*5)

'''a = int(input("Enter first no. : "))
b = int(input("Enter second no. : "))
opr = str(input("Enter the operation you want to perform : "))

if (opr == "+") {
    print("The sum of ",a," and ",b," is : ", a+b)
}
else if (opr == "-") {
    print("The subtraction of ",a," and ",b," is : ", a-b)
}
else if (opr == "*") {
    print("The multiplication of ",a," and ",b," is : ", a*b)
}
else if (opr == "/") {
    print("The division of ",a," and ",b," is : ", a/b)
}
else {
    print("Wrong operation")
}
'''


'''letter = "Dear <|NAME|>
You are selected
Date: <|DATE|>"
name = input("Enter your name: ")
date = input("Enter Today's date: ")

letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)'''

'''st = input("Enter any string: ")

doubleSpaces = st.find("  ")
st = st.replace("  "," ")
print(st)'''

# letter = "Dear Tanisha, This python tutorial is going nice. Thanks"
# print(letter)
# for_letter = "Dear Tanisha,\n\tThis python tutorial is going nice.\n\tThanks"
# print(for_letter)


#to create a list use: []
a = [ 1, 4, 6, 7, 36, 78, 87 ]

# #to print the list use:
# print(a)

# #to print any value from list use:
# print(a[3])

# #to chnge the value in list at any particular index use:
# a[3] = 5
# print(a)

# #we can create a list with values of diferent datatypes
# x = ["tanisha", 10, "July", 2002]
# print(x)

# #list slicing
# friends = ["tanisha", "neha", "riya", "ruhani", "heena"]
# print(friends[0:3])

'''list methods
a.reverse() t reverse the order of the list
print(a)

a.append(39) to add something in list
print(a)

a.insert(3,56) to add some value(56) at a particular index(3)
print(a)

a.sort() to sort the list
print(a)

a.pop() to pop out the last or top value from list
print(a)

a.remove(7)
print(a)'''

# tuple: it is a immutable data type in python.
# one it is initialised it can not be changed.
# tuples are initialised with round bracket().

t = (1, 3, 5, 6)
# t1 = () empty tuple
# t1 = (3, ) for single element in tuple we hae to add a comma to it.

# t[0] = 4 throws an error
# print(t.count(1)) to count the no of values repeated
# print(t.index(5)) to find the index of any value

# pr1
'''f1 = input("Enter Fruit No. 1: ")
f2 = input("Enter Fruit No. 2: ")
f3 = input("Enter Fruit No. 3: ")
f4 = input("Enter Fruit No. 4: ")
f5 = input("Enter Fruit No. 5: ")
f6 = input("Enter Fruit No. 6: ")
f7 = input("Enter Fruit No. 7: ")
f8 = input("Enter Fruit No. 8: ")

myFruitList = [f1, f2, f3, f4, f5, f6, f7, f8]
print(myFruitList)'''

# pr2
'''m1 = int(input("Enter your marks of 1 subject: "))
m2 = int(input("Enter your marks of 2 subject: "))
m3 = int(input("Enter your marks of 3 subject: "))
m4 = int(input("Enter your marks of 4 subject: "))
m5 = int(input("Enter your marks of 5 subject: "))
m6 = int(input("Enter your marks of 6 subject: "))

myMarks= [m1, m2, m3, m4, m5, m6]
myMarks.sort()
print(myMarks)'''

# pr3
# l1 = [2, 4, 6, 7]
# print(sum(l1)) to sum up the values of list

# a = (7, 0, 8, 0, 0, 9)
# print(a.count(0))

# Dictonary: combination of key(name) and value(tanisha)
# syntax: {"name":"value", "name2":"value2"}

'''myDict = {
    "name":"Tanisha",
    "rollNo":1907004,
    "anotherDict":{"Tanisha":"Programmar"}
}'''

# print(myDict['name'])

# myDict["rollNo"] = [1907004, 439]: dictonary is mutable
# print(myDict['rollNo'])
# print(myDict['anotherDict']['Tanisha']): nested dictonary

# Dictonary methods
'''
print(list(myDict.keys())): prints the keys of the dict as list
print(myDict.values()): prints the keys of the dict
print(myDict.items()): prints all the (key,values) of dict.
'''
# print(myDict)

# to update dict
'''updateDict = { 
    "lovish" : "Friend"
    }

myDict.update(updateDict)

'''

'''print(myDict.get("name")) #returns value associated to key(name)
print(myDict["name"])  #returns value associated to key(name)

print(myDict.get("name2")) #returns none as name2 is not present
print(myDict["name2"])  #throws an error as name2 is not present
'''
# a = {1,2,3,4,5}
# print(a)
# print(type(a))

# a = {1,2,3,4,5,3,4,1}: no duplication/repetition of values allowed

# it will create a empty dict not a empty set
# a = {}

# to create an empty set follow
'''b = set()
# print(type(b))

b.add(5) #to add values
b.add(7)
# print(b)

b.add((6,8,9))
# list and dict cannot be added in set
print(len(b)) #prints the length of the set

# b.remove(5) # only present elements can be removed otherwise it will show an error
print(b.pop())
'''
# pr1
'''myDict = {
    "kalam" : "pen",
    "pankha" : "fan",
    "rang" : "color"
}

print(myDict.keys())

x = input("Enter the key to know its value: ")
print(myDict.get(x))
# to avoid error
'''

# pr2

'''a1 = int(input("Enter 1 no.: "))
a2 = int(input("Enter 2 no.: "))
a3 = int(input("Enter 3 no.: "))
a4 = int(input("Enter 4 no.: "))
a5 = int(input("Enter 5 no.: "))
a6 = int(input("Enter 6 no.: "))
a7 = int(input("Enter 7 no.: "))
a8 = int(input("Enter 8 no.: "))

set = {a1, a2, a3, a4, a5, a6, a7, a8}

print(set)'''

# pr3

'''set = {18, "18"}
print(len(set))'''

# pr4

'''s = set()
s.add(20)
s.add(20.0)
s.add("20")

print(s)
print(len(s))'''

# pr5

'''k1 = input("Enter your name as key: ")
v1 = input("Enter your favourite language as value: ")
k2 = input("Enter your name as key: ")
v2 = input("Enter your favourite language as value: ")
k3 = input("Enter your name as key: ")
v3 = input("Enter your favourite language as value: ")
k4 = input("Enter your name as key: ")
v4 = input("Enter your favourite language as value: ")

myDict = {
    k1 : v1,
    k2 : v2,
    k3 : v3,
    k4 : v4
}

print(myDict)
print(myDict.keys())
print(myDict.values())'''

# Conditional Statement: if-elif-else statement.
a = 8

# 1. if-elif ladder
'''
if (a>3):
    print("The value is greater than 3")
elif(a>7):
    print("The value is greater than 7")
else:
    print("The value is not greater than 3 and 7")
'''

# 2. Multiple if statements
'''if (a>3):
    print("The value is greater than 3")

if(a>7):
    print("The value is greater than 7")
else:
    print("The value is not greater than 3 and 7")'''
   
# -------------------------------------------------------- #
'''age = int(input("Enter your age: "))

if(age>18):
    print("Yes")
else:
    print("No")'''

# -------------------------------------------------------- #

# is and in
'''a = None

if a is None:
    print("yes")
else:
    print("no")
    
a = [89,67,6,46,88,34]
print(859 in a)
'''
# pr1

'''n1 = int(input("enter 1 no.: "))
n2 = int(input("enter 2 no.: "))
n3 = int(input("enter 3 no.: "))
n4 = int(input("enter 4 no.: "))

if(n1>n2 and n1>n3 and n1>n4):
    print(n1, " is greater")
elif(n2>n3 and n2>n4):
    print(n2, " is greater")
elif(n3>n4):
    print(n3, " is greater")
else:
    print(n4, " is greater")'''

# pr2

n1 = int(input("enter 1 no.: "))
n2 = int(input("enter 2 no.: "))
n3 = int(input("enter 3 no.: "))