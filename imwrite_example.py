import cv2
img = cv2.imread("anand.jpeg",-1)
cv2.imshow("anand", img)
k=cv2.waitKey(0) 
if k==27:
    cv2.destroyAllWindows() 
elif k==ord('s'):
    cv2.imwrite('anand_copy.png', img)
    cv2.destroyAllWindows()
