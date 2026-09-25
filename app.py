import streamlit as st
from google import genai

# Page config
st.set_page_config(page_title="FitBuddy AI")
st.title("FitBuddy - Your AI Fitness Assistant")

# Get key
api_key = st.secrets["GEMINI_API_KEY"]

# New client method
client = genai.Client(api_key=api_key)

question = st.text_input("What is your question?")

if st.button("Ask"):
    if question:
        with st.spinner("Thinking..."):
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=question
            )
            st.write(response.text)
else:
    st.warning("please enter a question first!")
