import cv2
img=cv2.imread('colorpic.jpg')
while True:
    cv2.imshow('Different Color Image',img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()