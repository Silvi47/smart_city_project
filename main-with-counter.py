import cv2
import pandas as pd
import argparse
import numpy as np
from ultralytics import YOLO
from supervision import Detections
import torch
import torchvision
from tracker import *

WANTED_CLASS_ID_LIST = [
    1, # bicycle
    2, # car
    3, # motorcycle
    5, # bus
    7, # truck
]

vehicle_detection_model=YOLO('yolov8n.pt')
plate_detection_model=YOLO('model_best3.pt')

def filter_detections(detections: Detections, mask: np.ndarray) -> Detections:
  return Detections(
    xyxy=detections.xyxy[mask],
    confidence=detections.confidence[mask],
    class_id=detections.class_id[mask],
    tracker_id=detections.tracker_id[mask]
    if detections.tracker_id is not None
    else None,
  )

def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        colorsBGR = [x, y]
        print(colorsBGR)

area_c = set()

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=True, help="Path to the file")
args = vars(ap.parse_args())

cap=cv2.VideoCapture(args["file"])

count=0
tracker=Tracker()

area1 = [(216, 1),(307,1),(307,499),(216,499)]
# area1 = [(195,294),(66,367),(708,449),(741,385)] #topleft, bottomleft, bottomright, topright

while True:    
    # looping video
    # if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT): #frame saat ini == total frame pd video
    #     cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    ret,frame = cap.read()
    if not ret:
        break
    count += 1
    if count % 3 != 0:
        continue
    
    frame=cv2.resize(frame,(1020,500))
    # results=vehicle_detection_model.predict(frame)
    results = vehicle_detection_model(frame)[0]
    vehicle_detections = Detections.from_yolov8(results)

    # Apply NMS and filter detections from unwanted classes
    kept_box_idxs = torchvision.ops.nms(torch.from_numpy(vehicle_detections.xyxy), torch.from_numpy(vehicle_detections.confidence), iou_threshold=0.5)
    mask = np.array([
      class_id in WANTED_CLASS_ID_LIST and idx in kept_box_idxs
      for idx, class_id in enumerate(vehicle_detections.class_id)
    ], dtype=bool)
    vehicle_detections = filter_detections(detections=vehicle_detections, mask=mask)
    
    # print(vehicle_detections)
    a=torch.from_numpy(vehicle_detections.xyxy) #results[0].boxes.boxes
    print(a)
    
    px=pd.DataFrame(a).astype("float")
#    print(px)
    list=[]
    for index,row in px.iterrows():
        x1=int(row[0])
        y1=int(row[1])
        x2=int(row[2])
        y2=int(row[3])
        # d=int(row[5])
        # c=class_list1[d]
        list.append([x1,y1,x2,y2])
            
    bbox_idx=tracker.update(list)
    for bbox in bbox_idx:
        x3,y3,x4,y4,id=bbox
        cx=int(x3+x4)//2
        cy=int(y3+y4)//2
        results=cv2.pointPolygonTest(np.array(area1,np.int32),((x3,y3)),False)
        cv2.rectangle(frame,(x3,y3),(x4,y4),(0,255,0),2)
        cv2.circle(frame,(x3,y3),5,(255,0,255),-1)
        if results>=0:
            # Crop the frame and detect vehicles' plate
            vehicle_image = frame[y3:y4, x3:x4]
            plate_detections = plate_detection_model.predict(vehicle_image)[0]
      
            if (len(plate_detections) > 0):
                max_plate_detection_xyxy = plate_detections.boxes.xyxy[0] #[torch.argmax(plate_detections.boxes.conf)]
                x7, y7, x8, y8 = map(int, max_plate_detection_xyxy[:4])
                # plate_image = vehicle_image[y7:y8, x7:x8]
                cv2.rectangle(vehicle_image,(x7,y7),(x8,y8),(255,0,255),2)
                area_c.add(id)
                # cv2.imshow('Plate Image', plate_image)
    counting = (len(area_c))
    cv2.putText(frame,str(counting),(307,100),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,255),1)
    cv2.polylines(frame, [np.array(area1,np.int32)], True,(0,0,255),2)
    cv2.imshow("RGB", frame)

    k = cv2.waitKey(1)
    if k == ord("q"):
        break
