import cv2                                                 #importing cv2 module from opencv
img=cv2.imread('agenda.jpg', 1)                              # inserting an image into 'imag' variable
cv2.imshow('agendaa',img)                                     #showing the img variable 
k=cv2.waitKey(0)                                                #waitkey is the function which takes the time to destroy frame
if k==27:                                                        #k==27 means by clicking esc windows are destroyed
    cv2.destroyAllWindows()
elif k==ord('s'):                                                 #by clicking s img is saved into another
    cv2.imwrite('agenda-copy.jpg',img)
    cv2.destroyAllWindows()
