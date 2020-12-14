import datetime

def calcular(n):
   if n == 1: 
      return 1
   if n == 2:
      return 2
   if n == 3:
      return 4
   combinations = []
   combinations.append(1)
   combinations.append(2)
   combinations.append(4)
   x = 3
   while x < n:
      combinations.append(combinations[x-1]+combinations[x-2]+combinations[x-3])
      x += 1
   return int(combinations[n-1]) % 10000000007

t1 = datetime.datetime.now()
for a in range(1,2000):
   calcular(a)
   t2 = datetime.datetime.now()
   d = t2 - t1
   print(a,int(d.total_seconds()*1000))
