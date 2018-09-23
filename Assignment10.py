

#Question 1
f=open('test.txt')
lines=f.readlines()
print(lines)
x=int(input("ENTER: "))
for i in range(x):
    print(lines[i])
f.close()



#Question 2
li=[]
dic={}
f=open('test.txt')
data=f.read()
print(data)
li=(data.split())
for i in li:
    dic[i]=li.count(i)
print(dic)
f.close()


#Question 3
f=open('test.txt')
g=open('test1.txt','w')
data=f.read()
g.write(data)
g.close()
g=open('test1.txt')
data2=g.read()
print(data2)
g.close()
f.close()


#Question 4
f=open('test.txt')
g=open('test1.txt')
data=f.read()
data2=g.read()
print(data2)
a=data.split()
b=data2.split()
for i in range(len(a)):
    print(a[i]+b[i])
g.close()
f.close()


#Question 5
li3=[]
f=open('test.txt','w')
for i in range(10):
    a=input('Enter the numbers in the file')
    f.write(a)
    f.write('\n')
f.close()
f=open('test.txt')
data=f.read()
data2=data.split()
print(data2)
for i in data2:
    li3.append(int(i))
li3.sort()
print(li3)


