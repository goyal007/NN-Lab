#Back Propagation Algorithm (Assign-3)

import math
import numpy as np
def sigmoid(input):
    temp=(1/(1+(math.e**(-1*input))))
    return temp
c=0.9 #learning rate
d = 1 # Target

weight_hidden = []
weight_output= []
bias_hidden = []
bias_output = []
#w=np.array(w)

input_nodes = int(input("enter input nodes"))
hidden_nodes = int(input("enter hidden nodes"))

x=[]
print("enter input nodes values")
for j in range(input_nodes):
    x1 = float(input())
    x.append([x1])                         
x=np.array(x)
print(type(x))



for i in range(hidden_nodes):
    w1= []
    print("enter weight for",i+1," hidden node")
    for j in range(input_nodes):
        x1 = float(input())
        w1.append([x1])
    w1 = np.array(w1)
    weight_hidden.append(w1)


w1= []
print("enter weight for output node")
for j in range(hidden_nodes):
    x1 = float(input())
    w1.append([x1])
weight_output = np.array(w1)

print(weight_hidden)
print(weight_output)
#print(weight_hidden[0])
#print(weight_hidden[1])
#print(type(weight_hidden[0]))
#print(type(weight_hidden))

print("enter bias weight for hidden layer")
for j in range(hidden_nodes):
    x1 = float(input())
    bias_hidden.append(x1)

print("enter bias weight for output layer/node")
x1 = float(input())
bias_output = x1   


#output_final

for k in range(10):
    output_hidden_nodes = []
    hidden_input_layer = []
    ###########################Processing Hidden Layer##########################
    for i in range(hidden_nodes):
        net1=(np.transpose(weight_hidden[i])).dot(x)
        net1 = net1[0][0]
        #print(net1,type(net1))
        net1 = net1+bias_hidden[i]
        #print(net1,type(net1))
        O=sigmoid(net1)
        #print(O)
        output_hidden_nodes.append(O)
        hidden_input_layer.append([O])
    print(output_hidden_nodes)
    print(hidden_input_layer)
    hidden_input_layer = np.array(hidden_input_layer)

    ###########################Processing Output Layer##########################
    net1=(np.transpose(weight_output)).dot(hidden_input_layer)
    net1= net1[0][0]
    net1 = net1+bias_output
    print(net1)
    O=sigmoid(net1)
    print(O)
    output_final = O
    print(output_final)

    ########################################error computation for output##########################
    error_hidden = []
    #error_output

    error_output = output_final*(1-output_final)*(d-output_final)
    print ("error at output node is: ",error_output)
    if(abs(error_output) < 0.001):
        print("Stop ")
        break

    ########################################error computation for output##########################

    for i in range(hidden_nodes):
        err = output_hidden_nodes[i]*(1-output_hidden_nodes[i])*(error_output*weight_output[i][0])
        error_hidden.append(err)
        print(err)

    ########################################Weight Updates output layer##########################


    print("\nweight update between hidden and output\n")
    for i in range(hidden_nodes):
        print("Previuos weight output",weight_output[i][0])
        weight_output[i][0] = weight_output[i][0] + c*error_output*output_hidden_nodes[i]
        print("Updated weight output",weight_output[i][0])

    ########################################Weight Updates hidden layer##########################

    print("\nweight update between hidden and input\n")
    for i in range(hidden_nodes):
        for j in range(input_nodes):
            print("Previuos weight hidden",weight_hidden[i][j][0])
            weight_hidden[i][j][0] = weight_hidden[i][j][0] + c*error_hidden[i]*x[j][0]
            print("Updated weight hidden",weight_hidden[i][j][0])

    ########################################Weight Updates of bias of output layer##########################

    print("\nweight update bias output\n")
    print("Previuos bias output",bias_output)
    bias_output = bias_output +c*error_output
    print("Updated bias output",bias_output)

    ########################################Weight Updates of bias of hidden layer##########################

    print("\nweight update bias hidden\n")
    for i in range(hidden_nodes):
        print("Previuos bias hidden",bias_hidden[i])
        bias_hidden[i] = bias_hidden[i] +c*error_hidden[i]
        print("Updated bias hidden",bias_hidden[i])
        
    print("Epoch", k+1," completed")
    print("#############################################################################")
