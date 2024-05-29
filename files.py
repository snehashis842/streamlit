import pandas as pd
import streamlit as st 

st.subheader('Uplode your file here:')
uploded_file=st.file_uploader("uplode the csv file:",type=('csv','xlsx'))

st.subheader('Loading the csv file :')

if uploded_file is not None:
    df = pd.read_csv(uploded_file)
    st.table(df.head())
else:
    st.write('please uplode the csv file')

st.subheader('uplode image')
uplode_image=st.file_uploader("uplode ypur image file:",type=('jpg','jpeg','png'))

st.subheader('Uploded image:')

if uplode_image is not None:
    st.image(uplode_image)
else:
    st.write('Uplode your image')

st.subheader('uplode video')
uplode_video=st.file_uploader("uplode ypur video file:",type=('mkv','mp4'))

st.subheader('Uploded video:')

if uplode_video is not None:
    st.video(uplode_video)
else:
    st.write('Uplode your video')


st.subheader('uplode audio')
uplode_audio=st.file_uploader("uplode ypur audio file:",type=('mp3','wav'))

st.subheader('Uploded audio:')

if uplode_audio is not None:
    st.audio(uplode_audio)
else:
    st.write('Uplode your audio')






