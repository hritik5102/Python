import cv2
img = cv2.imread('dog.png',0)
while True:
    cv2.imshow('hritik',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()
        break
   
