import random
import datetime
import time
i=0
red=[]
print('--------开始选择红球-----------')
while i < 6:
    time.sleep(random.uniform(0,10.00))
    random.seed(time.time())
    r=random.randint(1,33)
    if r not in red:
        red.append(r)
    i=len(red)
red.sort()
print('--------开始选择蓝球-----------')
time.sleep(random.uniform(0,10.00))
random.seed(time.time())
b=random.randint(1,16)
print('红球是：'+str(red)+' 篮球是：'+str(b))
input('选号完成！')

    
    
