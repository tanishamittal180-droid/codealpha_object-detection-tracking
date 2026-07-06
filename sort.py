from filterpy.kalman import KalmanFilter
import numpy as np

class Sort:

    def __init__(self,
                 max_age=20,
                 min_hits=3,
                 iou_threshold=0.3):

        self.next_id = 1
        self.objects = {}

    def update(self, detections):

        results=[]

        for det in detections:

            x1,y1,x2,y2,conf=det

            matched=False

            center_x=(x1+x2)//2
            center_y=(y1+y2)//2

            for obj_id,data in self.objects.items():

                ox,oy=data

                distance=np.sqrt(
                    (center_x-ox)**2+
                    (center_y-oy)**2
                )

                if distance<50:

                    self.objects[obj_id]=(
                        center_x,
                        center_y
                    )

                    results.append(
                        [x1,y1,x2,y2,obj_id]
                    )

                    matched=True
                    break

            if not matched:

                self.objects[self.next_id]=(
                    center_x,
                    center_y
                )

                results.append(
                    [x1,y1,x2,y2,self.next_id]
                )

                self.next_id+=1

        return np.array(results)