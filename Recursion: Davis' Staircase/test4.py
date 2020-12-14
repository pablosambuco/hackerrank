import math
import datetime

def calcular(n):
   return 0 if n < 0 else 1 if n == 0 else int(calcular(n-1) + calcular(n-2) + calcular(n-3)) % 10000000007


t1 = datetime.datetime.now()
for a in range(1,30):
   calcular(a)
   t2 = datetime.datetime.now()
   d = t2 - t1
   print(a,int(d.total_seconds()*1000))
