def genperms(s,l,r,perm):
    if(l==r):
        perm.add("".join(s))
    else:
        for i in range(l,r+1):
            s[i],s[l]=s[l],s[i]
            genperms(s,l+1,r,perm)
            s[i],s[l]=s[l],s[i]
def genperm(s):
    perm=set()
    genperms(list(s),0,len(s)-1,perm)
    return perm
def checkifbalanced(s):
    stack=[]
    for i in range(0,len(s)):
        flag=(s[i]==")")
        if (len(stack)==0 and flag):
            return False
        elif (flag):
            stack.pop()
        else:
            stack.append("(")
        flag=False
    if(len(stack)==0):
        return True
    return False
def genBrackets(n):
    s=""
    for i in range(n):
        s+="()"
    perms=genperm(s)
    l=[]
    count=0
    for i in perms:
        if(checkifbalanced(i)):
            count+=1
            l.append(i)
    return count,l
print(genBrackets(2))
print(genBrackets(3))
print(genBrackets(5))
print(genBrackets(4))
print(genBrackets(1))
print(genBrackets(6))