from array import *


file = open('test.txt')
Lines = file.readlines()
 
count = 0

for i in Lines:
    print(i.strip())

a = []
tmp=""
for i in range(len(Lines)):
    tmp = Lines[i]
    split=tmp.split()
    a.append([(j) for j in split])
print(a)
print('\n')

def printIndex(a,n):
    temp=""
    for i in a[n]:
      temp+=i
      temp+=" "
    print(temp)

def printAll(a):
    for i in range (len(a)):
        printIndex(a,i)

printAll(a)
print('\n')

def printFind(a, str):
    for i in range (len(a)):
     for j in range(len(a[i])):
          if (a[i][j]==str):
           printIndex(a,i)
    print('\n')

printFind(a,'CamRanh')
printFind(a,'17/2')



