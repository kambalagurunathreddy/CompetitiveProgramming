def BinaryGap(x):
    x=abs(x)
    count=0
    maxCount=0
    while(x>0):
        t1=x&1
        if(t1==1):
            count+=1
        if (t1==0):
            if (count>maxCount):
                maxCount=count
        x=x>>1 
    return maxCount
print(BinaryGap(0))
print(BinaryGap(55))
print(BinaryGap(-5))
print(BinaryGap(12354))
print(BinaryGap(6))

