from random import *
import random
import numpy as np
from PIL import *
from matplotlib import pyplot as plt
import matplotlib.cm as cm

im = [255]*20000 +20000*[0]
random.shuffle(im)                  #randomizing 0s and 255s
im = np.reshape(im, (-1, 200))      #reshaping the array from 1D to 2D using numpy library
print (im)                          #printing the 2D array which has either 0s or 255s
image = plt.imshow(im, cmap = cm.Greys_r )
plt.title('Original Image')
plt.show(image)         #this is the image without any processing
print (np.shape(im))

#to check for 0s and nonzeros
for i in range(0,199,1):
    for j in range(0,199,1):
        if (im[i,j]!=0):            #each pixel if it is a zero or not
            if((im[i,j-1]+im[i,j+1]+im[i-1,j]+im[i+1,j])!=0):        #checking the neighbors
                im[i,j]=128         #halving the value
print im
image1 = plt.imshow(im, cmap = cm.Greys_r)        #printing the gray scale image
plt.title('Processed Image')
plt.show(image1)



