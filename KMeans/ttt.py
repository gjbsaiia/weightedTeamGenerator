import numpy as np
import sys
import os
import matplotlib.pyplot as mat

c = {}
d = {}
for i in range(10):
    c[i] = int(np.random.rand(1)*100)
    d[i]=i
print(c)

for cd in c:
    print(cd)
print(len(c.values()))
print(len(d.keys()))
mat.scatter(c.values(),d.keys())
mat.show()

