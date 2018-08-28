# Q-1 Reverse the List
l=[1,2,3,4,5]
print(list(reversed(l)))
# Q-2 Print all the uppercase letters from a string
str=input("Enter A string :- ")
for i in range(len(str)):
    if str[i].isupper():
        print(str[i])

# Q-3 Split and Store the Values After TypeCasting
s=input("Enter Values").split(",")
l1=[]
for i in s:
    l1.append(int(i))
print(l1)
# Q-4 Check for Palindrome
a='aba'
b=a[::-1]
if(a==b):
    print("string is palindrome")
else:
    print("string is not palindrome")

# Q-5 Understand Deep and Shallow Copy
from copy import *
print("DeepCopy:- ")
lst1 = ['a','b',['ab','ba']]

lst2 = deepcopy(lst1)

lst2[2][1] = "d"
lst2[0] = "c";

print(lst2)
print(lst1)
print("Shallow Copy:- ")
lst3=lst1
lst3[0]="hi"
print(lst3)
print(lst1)
