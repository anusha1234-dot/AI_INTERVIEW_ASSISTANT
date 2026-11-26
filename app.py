
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


```python
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    st.success("API Connection Successful")

except (KeyError, FileNotFoundError):
    st.error(
        "GROQ_API_KEY is missing. "
        "Add it to Streamlit Cloud → App Settings → Secrets."
    )
```
    st.stop()
role=st.selectbox("Select Job Role",[
    "Python Developer",
    "Java Developer",
    "Data Analyst",
    "machine learning engineer",
    "software Engineer",
    "Hr Executive"
])
if st.button("Genrative Interview Questions"):
   prompt="Genrative 5 interview questions for the role of " + role
   response=client.chat.completions.create(
       model="openai/gpt-oss-120b",
       messages=[
               {"role":"system","content":You are an expert technical interviwer"},
           {"role":"user"."content":prompt}
       ]
    )
    output=response.choices[0].message.content
    st.write(output)
