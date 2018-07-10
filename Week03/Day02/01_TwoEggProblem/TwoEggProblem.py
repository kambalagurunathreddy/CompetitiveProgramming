import math
def my_function(HighestFloor,FloorsCount):
   #Complexity-O(m*(n^2)) -m=no.of eggs n=no.of floors
   x=HighestFloor
   count=0
   k=math.ceil((((1+8*FloorsCount)**0.5)-1)/2)
   print("---",k)
   y=0
   while(y<x):
   	z=y
   	y=y+k
   	k=k-1
   	count=count+1
   if(x==y):
       return count
   count=count+(x-z)
   return count
for i in range(1,101):
    print(my_function(i,100),end=" ")
