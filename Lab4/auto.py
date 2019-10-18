#Auto Associated Memory (Assign-4)
import math
import numpy as np


def func(a,b):
    if(a>0):
        return 1
    elif (a<0):
        return -1
    else:
        return b

A1=[[-1],[1],[-1],[1]] 
A2=[[1],[1],[1],[-1]] 
A3=[[-1],[-1],[-1],[1]]

A1 = np.array(A1)
A2 = np.array(A2)
A3 = np.array(A3)

A = [A1,A2,A3]

m=3
p=4 # size of 1 input
T =(A[0]).dot(np.transpose(A[0]))
for i in range(1,3):
    T = T + (A[i]).dot(np.transpose(A[i]))
print(T)

inp = [[1],[1],[1],[-1]]
inp = np.array(inp)
#print(inp[0])
#print(inp[0][0])

out = []
for i in range(p):
    t = []
    t1 = T[:,i] # single row
    print(t1)
    t.append(t1) #1*4 matrix
    t = np.array(t)
    t = np.transpose(t)  #4*1 matrix
    val = func((np.transpose(inp)).dot(t),inp[i][0])
    out.append(val)

print(out)

