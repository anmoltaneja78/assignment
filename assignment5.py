
# Q-1 Verify Leap Year
year=int(input("Enter a year to check if its leap year"))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("LEAP YEAR!!!")
        else:
            print("NOT LEAP YEAR")
    else:
        print("LEAP YEAR!!!")
else:
    print("NOT LEAP YEAR")
    
# Q-2 Check Whether the Given Dimensions Are of Square or Rectangle
length=int(input("Enter length"))

breadth=int(input("Enter breadth"))

if(length==breadth):

    print("IT'S A SQUARE")

else:

    print("IT'S A RECTANGLE")
# Q-3 Determine the oldest and the youngest age 
x=int(input("Enter age of first person"))

y=int(input("Enter age of second person"))

z=int(input("Enter age of third person"))

if(x>=y and x>=z):

    print("First person is the oldest")

elif(y>=x and y>=z):

    print("Second person is the oldest")

else:

    print("Third person is the oldest")



if(x<=y and x<=z):

    print("First person is the youngest")

elif(y<=x and y<=z):

    print("Second person is the youngest")

else:

    print("Third person is the youngest")

# Q-4 Analyse the given data

age=int(input("Enter age"))

sex=input("Enter sex")

m=input("Enter marital status")

if(sex=='F'):

    print("Work in Urban Areas")

else:

    if(age>=20 and age<=40):

        print("Can work anywhere")

    elif(age>=40 and age<=60):

        print("Work in urban areas")

    else:

        print("Error")

# Q-5 cost problem

q=int(input("Enter quantity"))

c=100*q

if(c>1000):

    c=c-(c*0.1)

    print("Total cost is =",c)

else:

    print("Total cost is =",c)

# Q-6 Print user defined integers
li=[]

for i in range(10):

    a=int(input("Enter a number"))

    li.append(a)

print(li)

# Q-7 write infinite loop
while True:

    print("*")

# Q-8 Make a list which will store square of elements

a=[]

b=[]

num=int(input("enter number of elements"))

for i in range(num):

    c=int(input("enter number"))

    a.append(c)

for j in a:

    v=j*j

    b.append(v)

print(b)

# Q-9

li1=[]

li2=[]

li3=[]

li4=[]

a=int(input("Enter total number of inputs"))

for i in range(a):

    b=input("Enter elements of list")

    li1.append(b)

for i in li1:

    if(i.isdigit()):

        li2.append(i)

    elif(i.isalpha()):

        li3.append(i)

    else:

        li4.append(i)

print(li2)

print(li3)

print(li4)

# Q-10

p=[]

for i in range(1,101):

    if(i>1):

        flag=False

        for j in range(2,i):

            if(i%j==0):

                flag=True

        if not flag:

            p.append(i)

print(p)

# Q-11

for i in range(5):

    for j in range(i):

        print("*",end='')

    print()

# Q-12 
li8=[]

n=int(input("Enter number of elements of list"))

for i in range(n):

    a=int(input("Enter element"))

    li8.append(a)

num=int(input("Enter the number you want to delete from list"))

x=li8.count(num)

for i in range(x):

    y=li8.index(num)

    del(li8[y])

print(li8)
