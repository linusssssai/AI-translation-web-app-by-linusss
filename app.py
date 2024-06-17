import os
from dotenv import load_dotenv
import streamlit as st
import translation_agent as ta

load_dotenv()

PASSWORD = os.getenv("STREAMLIT_PASSWORD")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

def check_password():
    if st.session_state["password"] == PASSWORD:
        st.session_state.authenticated = True
        del st.session_state["password"]
    else:
        st.error("😕 Incorrect password")

if not st.session_state.authenticated:
    st.text_input("Password", type="password", on_change=check_password, key="password")
    st.stop()



import streamlit as st
import translation_agent as ta

st.title("Translation Agent")

source_text = st.text_area("Enter the text to translate:")
source_lang = st.text_input("Source Language (e.g., English):")
target_lang = st.text_input("Target Language (e.g., Spanish):")
country = st.text_input("Country (e.g., Mexico):")

if st.button("Translate"):
    if source_text and source_lang and target_lang and country:
        translation = ta.translate(source_lang, target_lang, source_text, country)
        st.success("Translation:")
        st.write(translation)
    else:
        st.error("Please provide all the inputs.")
