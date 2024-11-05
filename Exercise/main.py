## ADD DAY AND A LIVE TIMER TO THE CAMERA APP

import streamlit as st
import cv2
from datetime import datetime

st.header("Motion Detector")
camera_button = st.button("Start Camera")

if camera_button:
    st_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        now = datetime.now()

        cv2.putText(img=frame, text=now.strftime("%A"), org=(30,50), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(255,0,0))

        cv2.putText(img=frame, text=now.strftime("%H:%M:%S"), org=(30,80), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(255,255,255))

        st_image.image(frame)