import cv2
img=cv2.imread("solar-system.jpg")
cv2.putText(img,"sun",(100,50),cv2.FONT_HERSHEY_COMPLEX,1,(5,96,252))
cv2.putText(img,"mercury",(120,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(73,125,214))
cv2.putText(img,"venus",(160,180),cv2.FONT_HERSHEY_COMPLEX,1,(23,111,255))
cv2.putText(img,"earth",(260,270),cv2.FONT_HERSHEY_COMPLEX,1,(201,129,4))
cv2.putText(img,"mars",(370,255),cv2.FONT_HERSHEY_COMPLEX,0.7,(4,4,201))
cv2.putText(img,"jupiter",(470,50),cv2.FONT_HERSHEY_COMPLEX,1,(2,250,250))
cv2.putText(img,"saturn",(750,125),cv2.FONT_HERSHEY_COMPLEX,1,(2,250,250))
cv2.putText(img,"uranus",(950,130),cv2.FONT_HERSHEY_COMPLEX,1,(250,188,2))
cv2.putText(img,"neptune",(1100,150),cv2.FONT_HERSHEY_COMPLEX,1,(250,0,0))
cv2.imshow("output",img)
cv2.imwrite("Solar_systemposter.jpg",img)

cv2.waitKey(0)

