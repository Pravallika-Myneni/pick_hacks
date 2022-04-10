import streamlit as st
import pandas as pd
import numpy as np
from functions import *
import matplotlib.pyplot as plt
import plotly.express as px

cols = ['c','m','r','b', 'g']
labels=['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']

st.title('Emotion Analyzer')
sentence = st.text_area('Input your sentence here:')
if st.button("submit"):
    if sentence:
        emotions = get_emotion(sentence)
        st.write(emotions)