import streamlit as st 
import pandas as pd 
import numpy as np
import pyrebase

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

#init firebase &database
firebase = pyrebase.initialize_app(config)
db = firebase.database()



data1 = db.child("Kelas").get()
data = data1.val()
print (data)
print (type(data))



'''
#title
st.title ("""BsinG!""")

#kolom
opsi_kelas = "XA","XB","XC","XD"
kelas = st.selectbox ("Kelas : ", opsi_kelas)

sensor1, sensor2, sensor3 = st.columns(3)

with sensor1 :
    st.metric (label="SoundLevel 1", value="65 dB", delta = " -5 dB")
with sensor2 :
    st.metric (label="SoundLevel 2", value="70 dB", delta = " -1 dB")
with sensor3 :
    st.metric (label="SoundLevel 3", value="63 dB", delta = " 4 dB")  

'''
