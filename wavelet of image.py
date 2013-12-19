## 2D-Wavelet program for image in python
## To install python wavelet library for linux(ubuntu):
## goto terminal and type: sudo apt-get install python-pywt

import cv2                                                      # importing computer vision library
import pywt                                                     # importing python wavelet library
import numpy as np                                              # importing array library
import matplotlib.pyplot as plt                                 # importing ploting library

image = cv2.imread('test.jpg')                                  # read test image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)            # convert to double
cv2.imwrite('gray_image.png',gray_image)                        # save image
x=np.asarray(Image.open("gray_image.png").convert("L"))         # get image in array format
wp = pywt.WaveletPacket2D(data=x, wavelet='db1', mode='sym')    # defining wavelet package
plt.imshow(wp.data,plt.cm.gray)                                 # plot original image
plt.show()                        
plt.imshow(wp['a'].data,plt.cm.gray)                            # plot approximate decomposition of image
plt.show()
z=wp['h'].data
z[z<0.0]=0.0
plt.imshow(z,plt.cm.gray)                                       # plot horizontal decomposition of image
plt.show()
z=wp['v'].data
z[z<0.0]=0.0
plt.imshow(z,plt.cm.gray)                                       # plot vertical decomposition of image
plt.show()
z=wp['d'].data
z[z<0.0]=0.0
plt.imshow(z,plt.cm.gray)                                       # plot diagonal decmposition of image
plt.show()
