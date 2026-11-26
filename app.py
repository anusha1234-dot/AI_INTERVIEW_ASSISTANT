
import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="AI Interview Assistant",
    layout="centered"
)

st.title("AI Interview Assistant")

st.caption("Practice interviews with AI-integrated questions and constructive feedback.")

st.caption("Launched by Anusha A")
st.caption("department of AI & DS ")
try:
    client=Groq(api_key=st.secrets['GROQ_API_KEY'])
    st.write=("API Connection Successfull")
except (keyError, FileNotFoundError):
    st.error('GROQ_API_KEY is missing. Add it to Streamlit Cloud -> App settings Secrects ')
    st.stop()
