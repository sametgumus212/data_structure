import random
def MC_pi(n):
  cemberb=0
  cemberk=0
  sayacb=0
  sayack=0
  for i in range(1,n):
    x=10*random.random()
    y=10*random.random()
    ##print(x,y)
    if( x**2+y**2)<=3 :
        cemberb+=1
        sayacb+=1
    elif  (x**2+y**2)<=2:
        cemberk+=1
        sayack+=1
    else:
        pass
    b_oran_k=cemberb/cemberk
  print(b_oran_k)

MC_pi(100000)

sb=0
sk=0
for i in range(1000000):
    x=random.random()*10
    y=random.random()*10
    if (x**2+y**2)>1 and(x**2+y**2)<=4:
        sb+=1
    elif (x**2+y**2)<=1:
        sk+=1
print(sb/sk)
print(sb)
print(sk)