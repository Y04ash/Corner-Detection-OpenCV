import cv2
import numpy as np

img = cv2.imread('C:\\Users\\DELL\\Desktop\\yash\\python\\cv\\cornerDetection\\chessboard.webp')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 100,0.5,10)
# 100 is no of best corner to return 
# 0.01 is the confidence of the corner (how perfect it is (0-1))
# 10 is the min euclidian distance bw 2 corner 
# corners is the cods of such corners which is in float 

corners = np.int0(corners) # to convert float to int
# the returned arr will be a nested array like [[],[],[]...] in order to flat it use ravel func 

for corner in corners :
    x,y = corner.ravel()
    # draw a circle in x,y
    cv2.circle(img, (x,y), 5, (255,0,0),-1)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindow()
