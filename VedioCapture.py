import cv2
cap= cv2.VideoCapture(0);                                   #capturing vedio into cap variable
fourcc  = cv2.VideoWriter_fourcc('X','V','I','D')            #fourcc code
out= cv2.VideoWriter('out.avi',fourcc,20.0,(640,480))
while(cap.isOpened()):                                          #isOpened() should be true
    ret,frame=cap.read()
    if ret==True:
          print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
          print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
          out.write(frame)
          gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY )          #changing color model
          cv2.imshow('frame',gray)
          if cv2.waitKey(0) & 0xFF == ord('s'):
              break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
