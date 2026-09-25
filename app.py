import streamlit as st
from google import genai
st.title("FitBuddy")
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
q = st.text_input("Ask something")
if st.button("Ask"):
 r = client.models.generate_content(model="gemini-2.0-flash", contents=q)
 st.write(r.text)

