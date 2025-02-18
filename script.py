import streamlit as st
import os
import tempfile
from gtts import gTTS
import base64


# Function to generate speech using Google TTS
def tts(text, language):
    if not text:
        st.error("Please enter some text.")
        return None

    # Language codes for Google TTS
    lang_code = "en" if language == "English" else "kn"

    try:
        tts = gTTS(text=text, lang=lang_code)
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_file:
            tts.save(temp_file.name)
            temp_file_path = temp_file.name

        return temp_file_path

    except Exception as e:
        st.error(f"Error generating speech: {str(e)}")
        return None


# Streamlit UI
st.title("🗣️ English & Kannada Text-to-Speech")

# Dropdown for selecting language
language = st.selectbox("Select Language", ["English", "Kannada"])

# Text input box
text_input = st.text_area("Enter text")

# Generate Speech Button
if st.button("Translate & Speak"):
    audio_file = tts(text_input, language)

    if audio_file:
        st.audio(audio_file)  # Play the generated speech

        with open(audio_file, "rb") as f:
            audio_bytes = f.read()
        b64_audio = base64.b64encode(audio_bytes).decode()
        href = f'<a href="data:audio/mp3;base64,{b64_audio}" download="speech.mp3">Download Audio</a>'
        st.markdown(href, unsafe_allow_html=True)
