#!/usr/bin/env python3
import numpy as np 
import matplotlib.pyplot as plt 
from PIL import Image

my_2nd_array = np.array([[1,2],[3,4]])
print(my_2nd_array)

print(my_2nd_array.itemsize)
print(my_2nd_array.dtype)
#to optimize space used you may specify data type

a = np.array([[1,2],[3,4]], dtype='int16')
print(a.itemsize)
print(a.dtype)

#to access particular element 
print(a[1,1])
#to access particular column 
print(a[:,1])
#to have an array of all zeros
zArr =  np.zeros((5,5))
print(zArr)
#to have an array of all same number
someArr = np.full((5,5),89)
print(someArr)
#load file data
filedata = np.genfromtxt('data.txt', delimiter=',')
filedata = filedata.astype('int32')
print(filedata)

#load Image
pic = Image.open('image1.jpg')
print(pic)
picAr = np.asarray(pic)
print(picAr.shape)
plt.imshow(picAr)


picArr2 = picAr.copy()
picArr2[:,:,1] = 0 # for all pixel make green channel 0
plt.imshow(picArr2)
plt.show()#don't forget this .