import random


def rand7():
    return random.randint(1, 7)


def rand5():
    temp=rand7()
    if temp<=5:
        return temp
    else:
        return rand5()


print 'Rolling 5-sided die...'
print rand5()
