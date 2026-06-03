import streamlit as st
import edge_tts
import asyncio
import io
 
st.title(" حول النص إلى صوت!")
 
text = st.text_area("اكتب النص هنا:")
 
lang = st.selectbox("اختار اللغة:", ["عربي", "إنجليزي"])
 
VOICES = {
    "عربي": {
        
        " زارية (امرأة - السعودية)": "ar-SA-ZariyahNeural",
        " شاكر (رجل - مصر)":         "ar-EG-ShakirNeural",
        " سلمى (امرأة - مصر)":       "ar-EG-SalmaNeural",
    },
    "إنجليزي": {
        " غاي (رجل - أمريكا)":       "en-US-GuyNeural",
        " جيني (امرأة - أمريكا)":    "en-US-JennyNeural",
        " رايان (رجل - بريطانيا)":   "en-GB-RyanNeural",
        " ليبي (امرأة - بريطانيا)": "en-GB-LibbyNeural",
    },
}
 
voice_label = st.selectbox("اختار الصوت:", list(VOICES[lang].keys()))
voice_id = VOICES[lang][voice_label]
