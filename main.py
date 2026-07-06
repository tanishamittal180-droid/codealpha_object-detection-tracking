import cv2
import numpy as np
from ultralytics import YOLO
from sort import Sort
import pyttsx3
import pandas as pd
import sqlite3
import time
import os

# ==================================
# Voice engine
# ==================================

engine=pyttsx3.init()
engine.setProperty("rate",150)

# ==================================
# Create folders
# ==================================

folders=[
    "screenshots",
    "recordings"
]

for folder in folders:

    if not os.path.exists(folder):
        os.makedirs(folder)

# ==================================
# CSV setup
# ==================================

if not os.path.exists("detections.csv"):

    df=pd.DataFrame(
        columns=[
            "Time",
            "Object",
            "Track_ID"
        ]
    )

    df.to_csv(
        "detections.csv",
        index=False
    )

# ==================================
# Database setup
# ==================================

conn=sqlite3.connect(
    "detections.db"
)

cursor=conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS detections(

id INTEGER PRIMARY KEY AUTOINCREMENT,
time TEXT,
object_name TEXT,
tracking_id INTEGER

)
""")

conn.commit()

# ==================================
# Load YOLO
# ==================================

model=YOLO("yolov8n.pt")

# ==================================
# Tracker
# ==================================

tracker=Sort()

# ==================================
# Read labels
# ==================================

with open("coco.txt","r") as f:

    classNames=f.read().split("\n")

# ==================================
# Webcam
# ==================================

cap=cv2.VideoCapture(0)

width=640
height=480

cap.set(3,width)
cap.set(4,height)

# ==================================
# Save video
# ==================================

fourcc=cv2.VideoWriter_fourcc(*'XVID')

out=cv2.VideoWriter(
    'recordings/output.avi',
    fourcc,
    20,
    (width,height)
)

# ==================================
# Restricted area
# ==================================

zone_x1=150
zone_y1=100

zone_x2=500
zone_y2=350

# ==================================

previousTime=0

detected_ids=set()

trail_points={}

# ==================================

while True:

    success,img=cap.read()

    if not success:
        break

    currentTime=time.time()

    fps=1/(currentTime-previousTime+0.001)

    previousTime=currentTime

    detections=np.empty((0,5))

    labels=[]

    results=model(img,stream=True)

    for r in results:

        boxes=r.boxes

        for box in boxes:

            x1,y1,x2,y2=map(
                int,
                box.xyxy[0]
            )

            confidence=float(
                box.conf[0]
            )

            cls=int(
                box.cls[0]
            )

            label=classNames[cls]

            if confidence>0.5:

                currentArray=np.array(
                    [x1,y1,x2,y2,
                     confidence]
                )

                detections=np.vstack(
                    (
                        detections,
                        currentArray
                    )
                )

                labels.append(label)

    tracked=tracker.update(
        detections
    )

    # Draw restricted area

    cv2.rectangle(
        img,
        (zone_x1,zone_y1),
        (zone_x2,zone_y2),
        (0,0,255),
        3
    )

    cv2.putText(
        img,
        "Restricted Zone",
        (zone_x1,
         zone_y1-10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0,0,255),
        2
    )

    # ==========================

    totalObjects=len(
        tracked
    )

    for i,obj in enumerate(tracked):

        x1,y1,x2,y2,trackID=obj

        x1,y1,x2,y2,trackID=map(
            int,
            [x1,y1,x2,y2,trackID]
        )

        centerX=(x1+x2)//2
        centerY=(y1+y2)//2

        if len(labels)>0:

            label=labels[
                min(
                    i,
                    len(labels)-1
                )
            ]

        else:

            label="Object"

        # Bounding box

        cv2.rectangle(
            img,
            (x1,y1),
            (x2,y2),
            (0,255,0),
            2
        )

        cv2.putText(
            img,
            f"{label} ID:{trackID}",
            (x1,y1-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255,255,0),
            2
        )

        # Center point

        cv2.circle(
            img,
            (centerX,centerY),
            5,
            (255,0,255),
            -1
        )

        # Trail tracking

        if trackID not in trail_points:

            trail_points[trackID]=[]

        trail_points[
            trackID
        ].append(
            (
                centerX,
                centerY
            )
        )

        for point in trail_points[trackID]:

            cv2.circle(
                img,
                point,
                3,
                (255,0,0),
                -1
            )

        # Intruder detection

        if (
            centerX>zone_x1 and
            centerX<zone_x2 and
            centerY>zone_y1 and
            centerY<zone_y2
        ):

            cv2.putText(
                img,
                "INTRUDER ALERT",
                (180,50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,0,255),
                3
            )

            if trackID not in detected_ids:

                detected_ids.add(
                    trackID
                )

                # Voice alert

                engine.say(
                    f"{label} detected"
                )

                engine.runAndWait()

                # Screenshot

                cv2.imwrite(
                    f"screenshots/{label}_{trackID}.jpg",
                    img
                )

                # CSV save

                row=pd.DataFrame({

                    "Time":[
                        time.strftime(
                            "%H:%M:%S"
                        )
                    ],

                    "Object":[
                        label
                    ],

                    "Track_ID":[
                        trackID
                    ]

                })

                row.to_csv(
                    "detections.csv",
                    mode='a',
                    index=False,
                    header=False
                )

                # Database save

                cursor.execute(
                    '''
                    INSERT INTO detections
                    (time,
                    object_name,
                    tracking_id)

                    VALUES(?,?,?)
                    ''',

                    (
                        time.strftime(
                            "%H:%M:%S"
                        ),
                        label,
                        trackID
                    )
                )

                conn.commit()

    # ==================================

    cv2.putText(
        img,
        f"FPS:{int(fps)}",
        (20,30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255,0,0),
        2
    )

    cv2.putText(
        img,
        f"Objects:{totalObjects}",
        (20,70),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255,0,0),
        2
    )

    out.write(img)

    cv2.imshow(
        "AI Smart Surveillance System",
        img
    )

    if cv2.waitKey(1)==27:
        break

# ==================================

cap.release()

out.release()

conn.close()

cv2.destroyAllWindows()