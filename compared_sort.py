import random
import time
from insertion_sort import *
from selection_sort import *
from quick_sort import *
from merge_sort import *

ary=[]
ary2=[]
ary3=[]
ary4=[]
for i in range(50000):
    r=random.randint(1,50000)
    ary.append(r)
    ary2.append(r)
    ary3.append(r)
    ary4.append(r)

t1=time.time()
quick_sort(ary,0,len(arr)-1)
t2=time.time()

print('quick_sort time:',t2-t1)

t1=time.time()
merge_sort(ary4)
t2=time.time()
print('merge_sort time:',t2-t1)



t1=time.time()
insertion_sort(ary2)
t2=time.time()


print('insertion_sort time:',t2-t1)
t1=time.time()
selection_sort(ary3)
t2=time.time()
print('selection_sort time:',t2-t1)

