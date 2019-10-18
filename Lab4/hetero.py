#Hetero Associated Memory (Assign-4)
import math
import numpy as np

def func(inp):
    size = inp[0].size
    result = []
    temp= []
    for i in range(size):
        if(inp[0][i] > 0):
            temp.append(1)
        else:
            temp.append(-1)
    result.append(temp)
    result = np.array(result)
    return result

A1=[[1,-1,-1,-1,-1,1]] 
A2=[[-1,1,1,-1,-1,-1]] 
A3=[[-1,-1,1,-1,1,1]]
A1 = np.array(A1)
A2 = np.array(A2)
A3 = np.array(A3)
A = [A1,A2,A3]

B1 = [[1,1,-1,-1,-1]]
B2 = [[1,-1,1,-1,-1]]
B3 = [[-1,1,1,1,-1]]
B1 = np.array(B1)
B2 = np.array(B2)
B3 = np.array(B3)
B = [B1,B2,B3]


M =(np.transpose(A[0])).dot(B[0])
for i in range(1,3):
    M = M + (np.transpose(A[i])).dot(B[i])
print(M)

alpha = [[-1,-1,-1,-1,-1,-1]]
alpha = np.array(alpha)
temp = alpha.dot(M)
beta = func(temp)
print(beta)
while(1):
    temp = beta.dot(np.transpose(M))
    alpha1 = func(temp)
    temp1 = alpha1.dot(M)
    beta1 = func(temp1)
    if(np.array_equal(beta,beta1)):
        print("same")
        break
    beta = beta1
print(beta)


'''
a=[[1,1]]
b=[[1,2]]

a=np.array(a)
b=np.array(b)
print(np.array_equal(a,b))
'''
