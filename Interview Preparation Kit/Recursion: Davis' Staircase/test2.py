import math
import datetime

def calcular(n):
    q = 0
    pasos3 = int(n / 3)
    resto3 = n % 3
    i = pasos3
    while i >= 0:  # cantidad de 3
        j = (pasos3 - i) * 3 + resto3  # valor a completar
        pasos2 = int(j / 2)
        resto2 = j % 2
        x = pasos2
        while x >= 0:  # cantidad de 2
            y = (pasos2 - x) * 2 + resto2  # cantidad de 1
            aux = [3] * i + [2] * x + [1] * y
            largo = i+x+y
            perm = math.factorial(largo)/(math.factorial(i)*math.factorial(x)*math.factorial(y))
            q += perm
            x -= 1
        i -= 1
    return int(q)%10000000007
    
t1 = datetime.datetime.now()
for a in range(1,300):
   calcular(a)
   t2 = datetime.datetime.now()
   d = t2 - t1
   print(a,int(d.total_seconds()*1000))
    