a = "stringa con delle parole"
vocali = {i for i in a if i in 'aeiou'}

print(sorted(vocali))

x = [1,4,7,9]
y = {i: 5 for i in x}
print(y)

import sys

s = sum([i*i for i in range(1000)])
print(s)
print(sys.getsizeof([i*i for i in range(1000)]))
 
#generatore - unica differenza sono le ()
g = sum((i*i for i in range(1000)))
print(g)
print(sys.getsizeof((i*i for i in range(1000))))


# avviare un timer
from timeit import default_timer as timer

start = timer()
t = [i*i for i in range(1_000_000)]
end = timer()
print(end-start)

# avviare un timer con ciclo forstart = timer()
start = timer()
a = []
for i in range(1_000_000):
    a.append(i*i)
end = timer()

print(end-start)