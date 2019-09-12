#Perceptron Learning Rule (Assign-1)

def signum(input):
    if input>0:
        return 1
    else:
        return -1
import numpy as np
c=0.1 #learning rate
w=[[1],[-1],[0],[0.5]]
x1=[[1],[-2],[0],[-1]]
d1=-1
d2=-1
d3=1
d=[d1,d2,d3]
x2=[[0],[1.5],[-0.5],[-1]]
x3=[[-1],[1],[0.5],[-1]]

#print(type(w))
w=np.array(w)
x1=np.array(x1)
x2=np.array(x2)
x3=np.array(x3)
#print(type(w))

x=[x1,x2,x3]
for j in range(5):
    print("epoch", j+1)
    for i in range(3):
        net1=(np.transpose(w)).dot(x[i])
        #print(net1)
        r=signum(net1)
        r=d[i]-r
        w= w + c*r*x[i]
        print(w)

