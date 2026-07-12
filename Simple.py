'''
a = 100
if a==100:
    print ("The given number is equal to 100")
else:
    print ("The given number is not equal to 100")
'''
'''
age = 19
voter = "No"

if age > 18:
    if voter=="yes":
        print("eligible for voting")
    else:
        print("please get you voter id")
else:
    print("you are not eligible for voting")
'''
'''
for i in range (5,1,-1):
    print(i)

a="Python"
for i in a:
    print(i,end="")
'''
'''
for i in range(1,5,2):
    print("hi")
'''
'''
for i in range(5 ,  0 ,-1):
    for j in range (0,i):
        print("*",end="")
    print()
'''
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
'''
'''
for i in range(6,1,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()
'''
'''
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end="")
    print()

a=1
while a<=5:
    print (a)
    a+=1

b = 5
while b>=1:
    print(b)
    b-=1
    
c=10
while c>=5:
    print(c)
    c+=1
'''


#a=5
#print(a)





#help("keywords")







'''

a=["Apple", "Banana", "Cherry"]
b=["Brinjal", "Tomato", "Carrot"]
c=a
print(c is a)  #True
print(a is c)  #False
print(a==b)  #False
'''
'''
for i in range(1,6):
    if i==3:
        break
    print(i)





fruits = ["apple","banana","cherry"]
for x in fruits:
    if x=="banana":
        continue
    print(x)


a=121
c=0
t=a
while t>0:
    d=t%10
    c=c*10+d
    t=t//10
print(c)
if a==c:
    print("Given number is a palindrome")
else:
    print("Not a palindrame")
'''

'''
a="livewire"
print(a . capitalize())
#To write a capital letter in the first letter of the string
print(a . upper())
print(a . lower())
print(a . isupper())#returns Boolean
print(a . islower())
b="1234"
print(b . isdigit())# if integer into the string returns true
print(a . isalpha())
c="15dk"
print(c . isalnum())
'''
'''
a="livewire"
#length starts from 1
print(len(a))
#center it gives hello world in center
#21-total length(letter)
#21-11=10
print(a.center(21,'*'))
#in hello world how many times 'l' is there
#to print that l count
print(a.count('l'))
print(a.count('a'))
#index starts from 0
#index must be str,not int
#l index-->h=0 e=1 l=2
print(a.index('l'))
#to print 3rd l index
print(a.index('e',1))
'''
'''
a=" livewire"
print(a.swapcase())
print(a.split("e"))
print(a.strip())
b=['Mohan','Naveen','Jothika']
print('-'.join(b))
'''
'''
s='student'
print(s[1])
print(s[3])
#print(s[7])
'''
'''
a="livewire"

print(a[0:4])
print(a[2:6])
print(a[::-1])
print(a[0:8:2])
print(a[:-1])
print(a[:-2])
print(a[1::3])


b=['Apple', 'Banana', 'Cherry','Dragon Fruit',89]

print(b[1])
print(b[0:4])
print(b[::-1])
print(b[:-1])
print(b[1::2])
print(b)


c=(1,2,3,9,5,6,7,8,9)
print(type(c))
print(c.count(9))
print(c.index(8))
'''
'''
a=[1,2,3,4,5,4]
print(a.index(4))
print(a.count(4))

print(a.remove(4))
print(a)
#a.pop(3)
a.pop()
print(a)

print(a.remove())
'''

'''
a={1,2,3,4}
b={4,5,6,8}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

print(a.symmetric_difference(b))
print(a.symmetric_difference_update(b))

a.update([3,4,5,6,7,8])
print(a)
print(a.symmetric_difference_update(b))
b.add(9)
print(b)

print(a.isdisjoint(b))

#print(a.issubset(b))
#print(a.issuperset(b))
'''
'''
a={1,2,3,4,5,6,7}
a.remove(5)
print(a)
a.pop()
print(a)
a.discard(6)
print(a)
'''
'''
a={1,2,3,4,5,6}
b={4,5,6}
print(a.isdisjoint(b))
print(b.isdisjoint(a))
print(a.issubset(b))
print(b.issubset(a))
print(b.issuperset(a))
print(a.issuperset(b))
'''

x={1,2,3,4,5}
y={4,5,6,7,8}


print(x.intersection(y))
print(x)

x.intersection_update(y)
print(x)


'''
#x.difference_update(y)
#print(x)

a={"apple","banana","cherry"}
b={"Microsoft","Google","apple"}
#a.intersection_update(b)
print(a)
'''

fruits = ["apple","banana","cherry"]
for x in fruits:
    if x=="banana":
        pass
    print(x)
