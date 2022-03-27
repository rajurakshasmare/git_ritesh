pairs1 = [(x,y) for x in range(9834,0,-8) for y in range (8624,0,-4) if (x+y)%3==0]
print(pairs1)
import sys
sys.exit(0)

pairs = [(x,y) for x in range(3,0,-1) for y in range (2,0,-1) if (x+y)%3==0]
print(pairs)

import sys
sys.exit(0)
x = [1,"abcd",2,"efgh",[3,4]]
y = x[0:50]
z = y
w = x
x[1] = x[1] +'d'
y[2] = 4
#x[1][1] = 'y'
z[0] = 0
w[4][0] = 1000
a = (x[4][1]==4)
print(x)
import sys
sys.exit(0)
i = 200
n = 80
while i >= n:
    i = i - 2
    n = n + 1




def myfunc(L):
    newL = []
    for i in L:
        if i not in newL:
            newL.append(i)
    return newL
L = [15,67,81,97,15,99,81,15,104,125,81,125]
print(myfunc(L))

import sys
sys.exit(0)

pairs = [(x,y) for x in range(3,0,-1) for y in range (2,0,-1) if (x+y)%3==0]
print(pairs)


pairs1 = [(x,y) for x in range(9834,0,-8) for y in range (8624,0,-4) if (x+y)%3==0]
print(pairs1)





p = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(p[1][1])
import sys
sys.exit(0)
i = 200
n = 80
while i >= n:
    i = i - 2
    n = n + 1


import sys
sys.exit(0)

def chatmsg(start):
    finalmsg = " "
    for i in range(0,len(start)):
        finalmsg = start[i] + finalmsg
    return finalmsg
str_1 = "hello"
str_2 = []
for i in range(len(str_1)):
    str_2.append(str_1[i])
exc = str_2
print(chatmsg(exc))








import sys
sys.exit(0)

x = [1,"abcd",2,"efgh",[3,4]]
y = x[0:50]
z = y
w = x
x[1] = x[1] +'d'
y[2] = 4
x[1][1] = 'y'
z[0] = 0
w[4][0] = 1000
a = (x[4][1]==4)
print(x)
import sys
sys.exit(0)

x = [13,4,17,1000]
w = x[1:]
u = x[1:]
y = x
u[0] = 50
y[1] = 40

print(x)














import sys
sys.exit(0)

s = input("Enter some string:")
s1=s2=output=''
for x in s:
    if x.isalpha():
        s1 = s1+x
    else:
        s2 = s2+x
for x in sorted(s1):
    output = output+x
for x in sorted(s2):
    output = output+x
print(output)



s1 = input("Enter First string:")
s2 = input("Enter Second string:")
output = ''
i,j = 0,0
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output = output+s1[i]
        i+=1
    if j<len(s2):
        output = output+s2[j]
        j+=1
        print(output)

s = input("Enter some string:")
print("characters at even position:",s[0::2])
print("characters at odd position:",s[1::2])

s = " durga software solutions pvt ltd"
l = s.split()
for x in l:
    print(x)

print(l)
s = "22-5-2021"
l = s.split('-')
print(l)
for x in l:
    print(x)
x = " python "
p = x.split()
print(p)

t = ('sunny','bunny','chinny')
s = '-'.join(t)
print(s)
l = ['hydrabad','singapore','london','dubai']
s = ':'.join(l)
print(s)
s = 'learning python is very easy'
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.capitalize())
s = 'learning python is very easy'
print(s.startswith('learning'))
print(s.endswith('learning'))
print(s.endswith('easy'))
s = input("Enter some string:")
print(s[::-1])
x = "raju do fast you dont have time"
print(x[::-1])
s = input("Enter some string")
print(''.join(reversed(s)))


s = input("Enter some string:")
i = len(s)-1
target = ''
while i>0:
    target = target+s[i]
    i = i-1
    print(target)









import sys
sys.exit(0)





s = 'Raju'
print(s[3])
x = "hey how are you"
print(x[8])
print(x[-2])
print(x[9])
s = "Learning python is very easy when you do hard work"
print(s[1:7:5])
print(s[1::7])
print(s[::-1])
print(s[::-2])
print(s[::-5])
print(s[::1])
print(s[::2])
print(s[::3])
print(s[::1])
print(s[1:7])
print(s[2:5:2])
s = 'abcdefghijklmnopqrstuvwzyz'
print(s[1:6:2])
print(s[1:2:2])
print(s[::1])
print(s[::-1])
print(s[::-2])
print(s[::-3])
print(s[::-4])
print(s[::-6])
print(s[::-4])
print(s[::4])
s = 'Learning python is very easy'
n = len(s)
i = 0
print("Forward direction")
while i<n:
    print(s[i],end='')
    i+=1
print("Backward direction")
i=-1
while i>=n:
    print(s[i],end='')
    i=i-1

s = "Learning python is very easy"
print("forward direction")
for i in s:
    print(i,end='')
print("Forward direction")
for i in s[::]:
    print(i,end='')
print("Backward direction")
for i in s[::-1]:
    print(i,end='')
s = input("enter main string:")
subs = input("Enter sub string:")
if subs in s:
    print(subs,"is found in main string")
else:
    print(subs,"is not found in main string")

s1 = input("Enter first string:")
s2 = input("Enter second string")
if s1==s2:
    print("Both string are equal")
elif s1>s2:
    print(" first string is greater than second string")
else:
    print("first string is less than second string")
city = input("Enter your city name")
scity = city.strip()
if scity=='Hyderabad':
    print("Hello Hydderabadi....Adab")
elif scity=='Chennai':
    print("Hello madrasi.....Vannakam")
elif scity=="Bangalore":
    print("Hello Kannan....shubodaya")
else:
    print("your entered city is invalid")

s = input("Enter main string:")
subs = input("Enter sub string:")
try:
    n = s.index(subs)
except ValueError:
    print("substring not found")
else:
    print("substring found")

s = input("Enter main string:")
subs = input("Enter sub string:")
flag = False
pos = -1
n = len(s)
while True:
    pos = s.find(subs,pos+1,n)
    if pos==-1:
        break
    print("Found at position",pos)
    flag = True
    if flag == False:
        print("Not Found")

