import math
import datetime

def recursiva_del_orto(n,m):
    res=[]
    a=int(n/m)
    i=0
    if m == 1:
       res.append([n,n,m,[]])
    else:
        while i<=a:
            r=n- i*m
            for x in recursiva_del_orto(r,m-1):
                res.append([n,i,m,x])
            i+=1
    return res

def calcular(n,m=3):
    tot=0
    for x in recursiva_del_orto(n,m):
        n=1
        i=0
        l=0
        while i<m:
            if x[1] > 0:
               l+=x[1]
               n*=math.factorial(l)/(math.factorial(l-x[1])*math.factorial(x[1]))
            x=x[3]
            i+=1
        tot+=n
    return int(tot)

t1 = datetime.datetime.now()
for a in range(1,300):
   calcular(a)
   t2 = datetime.datetime.now()
   d = t2 - t1
   print(a,int(d.total_seconds()*1000))
