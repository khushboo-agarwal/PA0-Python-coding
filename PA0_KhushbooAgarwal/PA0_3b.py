#script to find if the randomly generated matrix is actually singular or not

import random
import numpy as np

#generating random matrix
a = np.random.randint(0,9, size=(3,3))
print a


#to calculate the determinant values
det = 0
detA = (a[1,1]*a[2,2]) - (a[2,1]*a[1,2])
detB = (a[1,0]*a[2,2]) - (a[2,0]*a[1,2])
detC = (a[1,0]*a[2,1]) - (a[1,1]*a[2,0])
det = (a[0,0]*detA)-(a[0,1]*detB)+(a[0,2]*detC)
if(det==0):                                         #condition for singularity of a matrix
    print("The matrix is singular")
else:
    print("The determinant value is ", det )


#note: This program solves the given question using the general determinant method