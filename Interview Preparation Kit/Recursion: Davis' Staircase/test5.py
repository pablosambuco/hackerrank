import datetime
import sys

sys.setrecursionlimit(5000)

def stepPerms(n):
   def innerStepPerms(n, counts):
      if n < 0:
         return 0
      if n == 0:
         return 1
      if n not in counts:
         counts[n] = innerStepPerms(n-3,counts) + innerStepPerms(n-2,counts) + innerStepPerms(n-1,counts)
      return counts.get(n)

   counts = {}
   return innerStepPerms(n, counts) % 10000000007
   



t1 = datetime.datetime.now()
for a in range(1,5001):
   stepPerms(a)
   t2 = datetime.datetime.now()
   d = t2 - t1
   print(a,int(d.total_seconds()*1000))
