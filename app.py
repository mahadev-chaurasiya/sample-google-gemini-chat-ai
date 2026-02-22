import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from PIL import Image

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-flash')

st.title("What can I help with?")

user_input = st.text_area("Ask a question:", height=150, placeholder="Type your message here...")

image_file = st.file_uploader("img", type=['png', 'jpg', 'jpeg'], label_visibility="collapsed")

audio_file = st.file_uploader("audio", type=['mp3', 'wav', 'ogg'], label_visibility="collapsed")

if user_input or image_file or audio_file:
    with st.spinner("Thinking..."):
        content = []
        
        if user_input:
            content.append(user_input)
        
        if image_file:
            image = Image.open(image_file)
            st.image(image, width=300)
            content.append(image)
        
        if audio_file:
            st.audio(audio_file)
            audio_data = {"mime_type": audio_file.type, "data": audio_file.read()}
            content.append(audio_data)
        
        response = model.generate_content(content)
        st.write(response.text)
