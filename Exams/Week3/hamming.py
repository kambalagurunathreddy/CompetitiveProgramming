def giveHammingDistance(x,y):
    if (x==y):
        return 0
    else:
        count=0
        while(x>0 or y>0):
            t1=x&1
            t2=y&1
            if(t1^t2==1):
                count+=1
            x=x//2 
            y=y//2
        return count

print(giveHammingDistance(25,30))
print(giveHammingDistance(1,4))
print(giveHammingDistance(25,30))
print(giveHammingDistance(100,250))
print(giveHammingDistance(1,30))
print(giveHammingDistance(0,255))



