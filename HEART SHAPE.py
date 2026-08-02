a=int(input("Enter a table length:"))
row=a*2
print(row)
col=row+1
print(col)
d=a//2
print("t",a+d)
f=d+1
print(d)
e=a//2-1
print(e)
mid1=a-e
mid2=a+e
print(mid1)
print(mid2)
last=col-(e+1)
print(last)
print("012345678910111213141516")

for i in range(d+1):
   for j in range(col):
      if i == 0 and not ((j>=0 and j<d)\
       or (j>=mid1 and j<=mid2)\
       or (j>=last and j<=col))\
       or i+j==d\
       or j-i==d+1\
       or j+i==a+d\
       or j-i==a+f:
            print("*",end="")
      else:
            print(" ",end="")
   print()
   
for i in range(a+1):
    for j in range(col):
       if(i==j or j+i==row):
           print("*",end="")
       else:
            print(" ",end="")
    print()