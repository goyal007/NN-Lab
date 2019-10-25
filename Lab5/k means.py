#k-means lustering algorithms (Assign-5)
import math
import numpy as np

def distance(a,b):
    x= abs(a[0]-b[0])
    y= abs(a[1]-b[1])
    z=x+y
    return z

points = [[2,2],[8,8],[7,7],[3,3],[2,3],[7,8]]

k = int(input("enter k value:"))
print("enter centroid values")

centroid = []
for i in range(k):
    x = int(input("enter X value:"))
    y = int(input("enter Y value:"))
    temp = [x,y]
    centroid.append(temp)

prev_centers = []
for i in range(k):
    temp= []
    prev_centers.append(temp)


for i in range(len(points)):
    temp_list = []
    for j in range(k):
        dist = distance(points[i],centroid[j])
        temp_list.append(dist)
    min_dist = min(temp_list)
    node = temp_list.index(min_dist)
    prev_centers[node].append(i)

print(prev_centers)

new_centers = []
for i in range(k):
    temp= []
    new_centers.append(temp)

while(1):
    centroid = []
    for i in range(k):
        list_nodes = prev_centers[i]
        size = len(list_nodes)
        x=0
        y=0
        for j in range(size):
            x = x + points[list_nodes[j]][0]
            y = y + points[list_nodes[j]][1]
        x = x/size
        y= y/size
        print(x,y)
        
        centroid.append([x,y])
    print(centroid)

    for i in range(len(points)):
        temp_list = []
        for j in range(k):
            dist = distance(points[i],centroid[j])
            temp_list.append(dist)
        min_dist = min(temp_list)
        node = temp_list.index(min_dist)
        new_centers[node].append(i)

    print(new_centers)
    c=0
    for i in range(k):
        if(np.array_equal(prev_centers[i],new_centers[i])):
            c=c+1
    if(c==k):
        break
    prev_centers = new_centers
    new_centers = []
    for i in range(k):
        temp= []
        new_centers.append(temp)
    print("c",c)
    
print("answer",new_centers)
        
