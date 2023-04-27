import os
import datetime
import cv2
directory__of__all__images='./dataset'
if not os.path.exists(directory__of__all__images):
    os.makedirs(directory__of__all__images)
total__number__of__sample=36
sample__per__upload=200
window=cv2.VideoCapture(0)
def update__dataset(character):
    if not os.path.exists(os.path.join(directory__of__all__images,str(character))):
        os.makedirs(os.path.join(directory__of__all__images,str(character)))
    print(f'collecting data for {character}........')
    done=False
    while True:
        success,frame=window.read()
        cv2.putText(frame,"press 'C' to start",(0,50),cv2.FONT_HERSHEY_DUPLEX,1.3,(0,0,255),2)
        cv2.imshow('window',frame)
        if cv2.waitKey(25)==ord('c'):
            break
    i=0
    while i < sample__per__upload:
        ret,frame=window.read()
        cv2.imshow('window',frame)
        cv2.waitKey(25)
        now=datetime.datetime.now()
        now=now.strftime("%d%m%Y%H%M%S")
        cv2.imwrite(os.path.join(directory__of__all__images,str(character),f'{now}_{i}.jpg'),frame)
        i+=1
    window.release()
    cv2.destroyAllWindows()