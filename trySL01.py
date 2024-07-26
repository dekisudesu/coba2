import pyrebase
from ultralytics import YOLO
import PIL
import cv2
import streamlit as st

#config firebase
config = {
    "apiKey": "AIzaSyALrAWJFvvAgJggC7zRWm1n2HSVvLDfJbw",
    "authDomain": "ambil-gambar-783c2.firebaseapp.com",
    "databaseURL": "https://ambil-gambar-783c2-default-rtdb.firebaseio.com",
    "projectId": "ambil-gambar-783c2",
    "storageBucket": "ambil-gambar-783c2.appspot.com",
    "messagingSenderId": "733768297155",
    "appId": "1:733768297155:web:0935579af1e0f953939076",
    "measurementId": "G-WJ0G1NM3NR"
}
kolA1, kolA2 = st.columns(2)
with kolA1:
    st.image ("LOGO SIC.png",width=150)
with kolA2 :
    st.title ("EAGLE VISION")

#init firebase
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
db = firebase.database()

img = storage.child("data/photo.jpg").download(" ", filename="photo.jpg")
jumlah_siswa = 25

model = YOLO("model1.pt")
uploaded_image = PIL.Image.open("photo.jpg")
res = model.predict(uploaded_image,conf=0.5,save=True)
box = res[0].boxes.xyxy.tolist()
res_plotted = res[0].plot()[:, :, ::-1]
st.image(res_plotted, caption='Foto Kelas',use_column_width=True)
st.write("Jumlah Siswa : "+str(len(box)))
st.write ("Jumlah Tidak masuk : "+str(jumlah_siswa-len(box)))
