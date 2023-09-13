import cv2

img=cv2.imread("4f.jpg")
greyImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
model=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
result=model.detectMultiScale(greyImg,1.1)
print(result)

for x,y,w,h in result:
       cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow("img",img)
cv2.waitKey(0)