def CountingBits(num):
    bitarray=[]
    for x in range(num+1):
        count=0
        while(x>0):
            t1=x&1
            if(t1==1):
                count+=1
            x=x>>1 
        bitarray.append(count)
    return bitarray
print(CountingBits(15))
print(CountingBits(16))
print(CountingBits(1))
print(CountingBits(25))
print(CountingBits(5))
print(CountingBits(6))
