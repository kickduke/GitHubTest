import random
import datetime
import time
i=0
j=0
seq=1
red=[]
blue=[]
def printlist(balllist):
    for l in balllist:
        print('%-2s' % str(l),end='  ')

print('红色球                  蓝色球')
while seq <= 5:
    red.clear()
    blue.clear()
    i=0
    j=0
    #--------红色球-----------
    while i < 5:
        time.sleep(random.uniform(0,1.00))
        random.seed(time.time())
        r=random.randint(1,35)
        if r not in red:
            red.append(r)
        i=len(red)
    red.sort()
    #--------蓝色球-----------
    while j < 2:
        time.sleep(random.uniform(0,1.00))
        random.seed(time.time())
        b=random.randint(1,12)
        if b not in blue:
            blue.append(b)
        j=len(blue)
    blue.sort()
    seq+=1
    printlist(red)
    print('     ',end='')
    printlist(blue)
    print('\n')
input('Done！')
