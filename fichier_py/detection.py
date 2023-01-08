import cv2
import torch
from tracker import *
import numpy as np
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

cap=cv2.VideoCapture('cctv.mp4')


def POINTS(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        colorsBGR = [x, y]
        print(colorsBGR)
        

cv2.namedWindow('FRAME')
#cv2.setMouseCallback('FRAME', POINTS)

tracker = Tracker()
area = [(377,315),(429,373),(535,339),(500,296)]
c = set()
while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(1020,500))
    cv2.polylines(frame,[np.array(area,np.int32)],True,(0,255,0),2)
    results = model(frame)
    #frame = np.squeeze(results.render())
    points = []
    for index , row in results.pandas().xyxy[0].iterrows():
        x1 = int(row['xmin'])
        y1 = int(row['ymin'])
        x2 = int(row['xmax'])
        y2 = int(row['ymax'])
        n=(row['name'])
        if 'person' in n:
            points.append([x1,y1,x2,y2]) 
            #cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,255),2)
            #cv2.putText(frame,str(n),(x1,y1),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)
    boxes_id = tracker.update(points) 
    #print(boxes_id)
    for box_id in boxes_id:
        x , y , w , h , idd = box_id
        cv2.rectangle(frame,(x,y),(w,h),(255,0,255),2)
        cv2.putText(frame,str(idd),(x,y),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),2)
        results = cv2.pointPolygonTest(np.array(area,np.int32),(w,h),False)
        #print(results)
        if results>= 0 :
            c.add(idd)
    #print(c) 
    a = len(c)
    cv2.putText(frame,'number of people is ='+str(a),(50,65),cv2.FONT_HERSHEY_PLAIN,3,(0,0,255),2)
    
    cv2.imshow('FRAME',frame)
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()
    