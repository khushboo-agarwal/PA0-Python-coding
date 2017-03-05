#Ant Problem
#assumptions: The length of each side is 1 mile, so the time interval and step length should be proportionately smaller
from __future__ import division
import math
import matplotlib.pyplot as plt

time_step = 0.005    #time for each step of simulation, by trial and error, the time is in hours
time_step1 = 0.007
time_step2 = 0.01
speed     = 1                   #the speed of each ant (equal to or less than 1 hour/mile


#length of a single step
L = speed*time_step
L1 = speed*time_step1
L2 = speed*time_step2

k = 0

def ant_path(l,k):

    # coordinates of each ant is given as follows
    x1 = 0
    y1 = 0
    x2 = 1
    y2 = 0
    x3 = 1/2
    y3 = math.sqrt(3)/2

    #graph plotting
    plt.axis([-1, 2, -1, 2])
    plt.plot([x1, x2, x3], [y1, y2, y3], 'ro')

    #the distance between two ants should be greater than L for the simulation to run and simultaneously, by manual calculations it was found that a minimum step distance
    #of 0.061 is needed otherwise the ants will not form the equilateral triangle
    while (math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))>= l+0.061):
        #we need to find the directions of each ant with respect to its previous ant, i.e. we need to get the angles
        #we calculate the slope of each ant; ant2 will differ by 2pi/3 from ant1; ant3 will differ by 2pi/3 from ant2; ant3 will differ
        #by 2*2pi/3 from ant1
        slope1 = (math.atan((y2 - y1)/(x2 - x1)))
        slope2 = slope1 + (2*math.pi)/3
        slope3 = slope1 + (4*math.pi)/3


        #new positions of the ants are given as follows:
        x1_new = x1+(l * math.cos(slope1))
        y1_new = y1+(l * math.sin(slope1))
        x2_new = x2+(l * math.cos(slope2))
        y2_new = y2+(l * math.sin(slope2))
        x3_new = x3+(l * math.cos(slope3))
        y3_new = y3+(l * math.sin(slope3))
        k = k+1

        #plot the points
        plt.plot([x1_new, x2_new, x3_new], [y1_new, y2_new, y3_new])
        plt.plot([x1_new, x2_new, x3_new], [y1_new, y2_new, y3_new], 'ro')


        x1 = x1_new
        x2 = x2_new
        x3 = x3_new
        y1 = y1_new
        y2 = y2_new
        y3 = y3_new

    plt.show()
    print("Total no. of steps =  ", k)
    time = k * time_step
    print("Time taken to meet =  ", time, 'hours')
    print("At 1 miles/hour speed, the ants traveled a distance of ", time, 'miles')


ant_path(L, k)


#this simulation shows that the ants move in smooth curve to reach the equialteral triangle's centroid where they all meet.

#NOTE: I tried to optimize the code but it takes a bit longer to run.