# Import necessary libraries
import streamlit as st
from pytube import YouTube

# Streamlit app
st.title("YouTube Video Downloader")

# Input box for the YouTube video URL
url = st.text_input("Enter YouTube Video URL:")

# Function to download the video
def download_video(url, download_path="."):
    try:
        st.info("Downloading... Please wait.")
        yt = YouTube(url)
        video_stream = yt.streams.filter(file_extension='mp4').first()
        video_stream.download(download_path)
        st.success("Download completed successfully!")
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Button to trigger the download
if st.button("Download"):
    download_video(url)
