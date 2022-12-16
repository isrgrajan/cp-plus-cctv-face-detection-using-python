#!/usr/bin/python

import sys
import cv2
import requests

def webcam_face_detect(video_mode, nogui = False, cascasdepath = "haarcascade_frontalface_default.xml"):

  face_cascade = cv2.CascadeClassifier(cascasdepath)
	cctv_ip="192.168.1.135" # replace it with your CCTV IP or hostname
	cctv_port="554" # don't replace port until you have changed it
	user_name="admin" # replace with your current CCTV Username
	user_pass="1234567" # replace with your current CCTV Password
	cctv_channel_no="1" # should be integer type
	use_subtype="0" # You can use 0 or 1, 0 user sub-stream & 1 means use main stream
	stream_url="rtsp://"+ user_name +":" + user_pass + requests.utils.quote("@") + cctv_ip + ":" + cctv_port + "/cam/realmonitor?channel=" + cctv_channel_no + "&subtype=" + use_subtype
    video_capture = cv2.VideoCapture(stream_url)
    num_faces = 0


    while True:
        ret, image = video_capture.read()

        if not ret:
            break

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor = 1.05,
            minNeighbors = 7,
            minSize = (10,10),
            flags=cv2.CASCADE_SCALE_IMAGE
            )

        num_faces = len(faces)
        if not num_faces == 0:
            print("num_faces\n")
            

        if not nogui:
            for (x,y,w,h) in faces:
                cv2.rectangle(image, (x,y), (x+h, y+h), (0, 255, 0), 2)

            cv2.imshow("Isrg Face Detector", image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    video_capture.release()
    cv2.destroyAllWindows()
    return num_faces


if __name__ == "__main__":
    if len(sys.argv) < 2:
        video_mode= 0
    else:
        video_mode = sys.argv[1]
    webcam_face_detect(video_mode)
