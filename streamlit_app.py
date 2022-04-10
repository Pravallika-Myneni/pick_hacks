import streamlit as st
from pydub import AudioSegment
from stt import *
from functions import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
        page_title="Bear_Assays",
        page_icon=":bear:",
        initial_sidebar_state="expanded",
    )

st.title("Bear_Assays")
st.subheader(":bear:")

st.header('How are you feeling today?')


cols = ['c','m','r','b', 'g']
labels=['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']

with st.form("gd"):
     slider_val = st.slider("Rate 1 - 10 how you are feeling", 1, 10)
     st.write("slider", slider_val)

     inp = st.radio('Select mode of input:', ['Voice', 'Text'])

     submit = st.form_submit_button("Option choosed")

     emotions = {
"Happy":0, 
"Angry":0 , 
"Surprise":0, 
"Sad":0, 
"Fear":0
}

     if(inp == 'Voice'):

          st.write("I'm all ears!")
          uploaded_file = st.file_uploader("Drop in a voice Note of how you are feeling today", type = ['mp3', 'wav', 'ogg', 'mp4'])
          submit_audio= st.form_submit_button("Upload Audio")

          if submit_audio:
               audio_file = open("audio_2.mp4", 'rb')
               st.audio(audio_file.read())

               #text = convert_speech_to_text("audio_2.mp4")
               text = "I am feeling great today"
               emotions = get_emotion(text)

               st.write(emotions)
          
     else:
          sentence = st.text_area('Input your sentence here:')
          if st.form_submit_button("submit"):
               if sentence:
                    emotions = get_emotion(sentence)
                    st.write(emotions)

    


st.title(" Understanding the relation between mood and fitness")

st.write(
     "Wellness is the act of practicing healthy habits on a daily basis to attain better physical and mental health outcomes, so that instead of just surviving, you're thriving. To understand the significance of wellness, it's important to understand how it's linked to health."
)

st.subheader("Let us use the data collected from a smart watch user to understand the realation")

health_df = pd.read_csv("25.csv")

corr = health_df.corr()
fig, ax = plt.subplots()
sns.heatmap(
    corr, 
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(20, 220, n=200),
    square=True,
    annot = True, 
    ax = ax
)


st.write(fig)