#Self Organizing maps (SOM) Assign-6

I1=[1,1,0,0]
I2=[0,0,0,1]
I3=[1,0,0,0]
I4=[0,0,1,1]
Inputs=[I1,I2,I3,I4]

W1=[0.2,0.6,0.5,0.9]
W2=[0.8,0.4,0.7,0.3]
Weights=[W1,W2]
m=len(Weights)   # number of output nodes (weights)
p=12       # iterations

def decider(val):
    if(val>=1 and val<=4):
        return 0.6
    elif(val>=5 and val<=8):
        return 0.5
    elif(val>=9 and val<=12):
        return 0.4
    
counter=0
loop = int(p/len(Inputs))
inputs_length = len(Inputs)

for i in range(loop):
    for j in range(inputs_length):
        counter=counter+1
        min_val=100000000000000
        update_unit=0
        for k in range(m):
            temp=0
            len_inp = len(Inputs[j])
            for t in range(len_inp):
                temp=temp+((Weights[k][t]-Inputs[j][t])**2)
            if(temp<min_val):
                min_val=temp
                update_unit=k+1
        print("Iteration Number - ",counter,"    Winner - ",update_unit)
        for t in range(len(Weights[update_unit-1])):
            Weights[update_unit-1][t]+=(decider(counter)*(Inputs[j][t]-Weights[update_unit-1][t]))
        for t in range(m):
            print("Weight",t+1,"-",Weights[t])
            
