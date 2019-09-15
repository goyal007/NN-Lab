#Single Layer Continuous Perceptron Training Algorithm (Assign-2)

import math

def sigmoid(input):
    temp=(2/(1+(math.e**(-1*input)))-1)
    return temp

import numpy as np
c=0.5 #learning rate
w=[[0],[0],[0],[0]]
x1=[[0],[0],[0],[1]]
x2=[[0],[0],[1],[1]]
x3=[[0],[1],[0],[1]]
x4=[[0],[1],[1],[1]]
x5=[[1],[0],[0],[1]]
x6=[[1],[0],[1],[1]]
x7=[[1],[1],[0],[1]]
x8=[[1],[1],[1],[1]]

d=[-1,1,-1,1,-1,1,-1,1]
#print(type(w))
w=np.array(w)
x1=np.array(x1)
x2=np.array(x2)
x3=np.array(x3)
x4=np.array(x4)
x5=np.array(x5)
x6=np.array(x6)
x7=np.array(x7)
x8=np.array(x8)
#print(type(w))

x=[x1,x2,x3,x4,x5,x6,x7,x8]
for j in range(200):
    print("epoch", j+1)
    count=0
    for i in range(8):
        net1=(np.transpose(w)).dot(x[i])
        #print(net1)
        O=sigmoid(net1)
        r=d[i]-O
        if(r!=0):
            count=1
        w= w + (c*r*x[i]*(1-O*O))/2
        for weight in w:
            print(weight[0],end="\t")
        print('\n')
    if(count==0):
        print("stop")
        break
            

