a=int(input("Enter a table length(make sure you enter only odd number):"))
row=a*2
col=row+1
d=a//2

f=d+1

e=a//2-1
mid1=a-e
mid2=a+e

last=col-(e+1)

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