import random


def rand5():
    return random.randint(1, 5)


def rand7():
     while (1==1):
            trial1=5*(rand5()-1)
            trial2=rand5()
            trial=trial1+trial2
            if trial <= 21:
                return trial%7+1


print 'Rolling 7-sided die...'
print rand7()
