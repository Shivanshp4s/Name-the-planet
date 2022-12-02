import cv2


img = cv2.imread("name the planets/solar-system.jpg")


text_2_show = "Sun"

cv2.putText(img,"Sun",(90,50),cv2.FONT_HERSHEY_TRIPLEX,1.7,(0,0,255))
cv2.putText(img,"Mercury",(110,190),cv2.FONT_ITALIC,0.5,(255,255,255))
cv2.putText(img,"Venus",(190,260),cv2.FONT_ITALIC,0.5,(255,255,255))
cv2.putText(img,"Earth",(290,260),cv2.FONT_ITALIC,0.5,(255,255,255))
cv2.putText(img,"Mars",(385,250),cv2.FONT_ITALIC,0.5,(255,255,255))
cv2.putText(img,"Jupiter",(495,100),cv2.FONT_ITALIC,0.5,(255,255,255))
cv2.putText(img,"Saturn",(700,100),cv2.FONT_ITALIC,0.5,(255,255,255))
cv2.putText(img,"Uranus",(965,130),cv2.FONT_ITALIC,0.5,(255,255,255))
cv2.putText(img,"Neptune",(1100,140),cv2.FONT_ITALIC,0.5,(255,255,255))

cv2.imshow("poster",img)

cv2.waitKey(0)
