# AI Smart Surveillance System using YOLO and Object Tracking

## Project Title
AI Smart Surveillance System with Real-Time Object Detection and Tracking

## Project Overview

This project is an advanced real-time AI surveillance system developed using Python, OpenCV, YOLOv8, and object tracking algorithms. The system captures live video from a webcam or video source, detects objects in real time, tracks them with unique IDs, and provides intelligent monitoring features.

The system can detect multiple objects simultaneously and assign tracking IDs for continuous monitoring.

---

## Features

✓ Real-time webcam/video processing

✓ YOLOv8 object detection

✓ Multiple object tracking

✓ Unique tracking IDs

✓ Bounding boxes and labels

✓ Confidence score display

✓ Object counting

✓ FPS (Frames Per Second) display

✓ Restricted area monitoring

✓ Intruder detection

✓ Voice alerts

✓ Screenshot capture

✓ Detection logs in CSV

✓ SQLite database storage

✓ Object movement trails

✓ Video recording

✓ Smart surveillance interface

---

## Technologies Used

Programming Language:

Python

Libraries:

OpenCV

Ultralytics YOLOv8

NumPy

Pandas

SQLite3

pyttsx3

FilterPy

SciPy

---

## Project Structure

AI_Smart_Surveillance/

├── main.py

├── sort.py

├── coco.txt

├── detections.csv

├── detections.db

├── screenshots/

├── recordings/

├── yolov8n.pt

├── README.rd

---

## Installation

Step 1: Clone project

```bash
git clone https://github.com/yourusername/AI_Smart_Surveillance.git
```

Step 2: Open project folder

```bash
cd AI_Smart_Surveillance
```

Step 3: Install dependencies

```bash
pip install ultralytics
pip install opencv-python
pip install numpy
pip install pandas
pip install pyttsx3
pip install scipy
pip install filterpy
```

Or install together:

```bash
pip install ultralytics opencv-python numpy pandas pyttsx3 scipy filterpy
```

---

## Running the Project

Run:

```bash
python main.py
```

Press:

```text
ESC
```

to stop the application.

---

## System Workflow

1. Webcam captures live video

2. Frames are passed to YOLOv8

3. Objects are detected

4. Bounding boxes are generated

5. SORT tracker assigns IDs

6. Object movement is tracked

7. Intruder zone monitoring occurs

8. Screenshots are captured

9. Detection logs saved in CSV

10. Detection data stored in database

11. Video recording is generated

---

## Dataset

YOLOv8 uses the COCO dataset containing 80 object classes including:

• Person

• Car

• Bicycle

• Dog

• Cat

• Bus

• Truck

• Mobile phone

• Laptop

and many more.

---

## Output

The system displays:

Real-time camera feed

Detected object labels

Tracking IDs

FPS counter

Object count

Restricted area alerts

Movement trails

---

## Example Output

Detected:

Person ID:1

Car ID:2

Dog ID:3

FPS:28

Objects:3

INTRUDER ALERT

---
## Screenshots
<img width="1366" height="768" alt="Screenshot 2026-07-06 130522" src="https://github.com/user-attachments/assets/e4aa504e-c2b7-4d5a-aa68-0bc98cb3061a" />

## Future Enhancements

1. Deep SORT tracking

2. Face recognition

3. Vehicle speed estimation

4. Heatmap visualization

5. Email alerts

6. WhatsApp notifications

7. Streamlit dashboard

8. CCTV/IP camera support

9. Cloud deployment

10. Mobile application integration

---

## Applications

Smart surveillance

Traffic monitoring

Security systems

Crowd monitoring

Retail analytics

Attendance systems

Industrial monitoring

Smart cities

---

## Author

Name: Tanisha Mittal

Project: AI Smart Surveillance System

Technology Stack:

Python | OpenCV | YOLOv8 | Machine Learning | Computer Vision
