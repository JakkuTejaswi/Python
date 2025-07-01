"""b=tuple(map(int,input().split(':')))


v=list[1,2.2,"Vl",True]

n=int(input("Enter you age:"))
if(n<18):
    print("Teenage")
elif(n>18 & n<50):
    print("Adult")
else:
    print("Old")
    """

""""l=[1,1,2,3,4,4,5,5,5]
s=set(l)
print(s)
if 2 in s:
    print("YES")
else:
    print("NO")"""
    
"""l=[1,2,1,2,2,3,3,4,5,6]
target=6
flag=0
for i in l:
   if(i==target):
        flag=1
if(flag==1):
    print("YES")
else:
    print("NO")
"""

"""for i in range(1,11):
    print(i,end=" ")"""

""""n=1
while(n<11):
    print(n,end=" ")
    n=n+1"""
    
"""a=[1,1,2,3,4,66,7]
b=len(a)
print(b)"""

"""a=[1,1,2,2,3,3,4,4,2,1]
target=2
count=0
for i in a:
    if(i==target):
        count=count+1
print(count)  """

"""a=[1,1,2,3,4,5,6,4,3]
d={}
for i in a:
    if i in d: 
        d[i]+=1
    else:
        d[i]=1
print(d)"""

a=[1,1,2,3,4,5,6,4,3]
min=a[0]
for i in a:
    if(i<min):
        min=i 
print(min)        

