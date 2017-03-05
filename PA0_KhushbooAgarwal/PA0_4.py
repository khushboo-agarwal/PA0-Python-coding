#Randomly generate a point in the square and count the number of times for a point to fall in an odd-numbered region

#Assumptions: the centre of the square is at (0,0) of the coordinate system; therefore the four vertices of the triangle
              # would be (-1,1), (1,1), (1,-1),(-1,-1)
              #the point will be denoted by (x,y)

import random
N = 1000000                 #no of tries
x=y=0
count = 0.0

for i in range(1,N,1):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if(x<0):
        count=count+1
    if(x>=0):               #the conditions
        if(x<=(1-y)):
            if(y>=0):
                count = count+1
print ("The count is " , count)     #output
prob = float(count/N)
print("The required probability is" , prob)
