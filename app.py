import streamlit as st
from google import genai

st.title("Fathima FitBuddy 💪")

# Load key from secrets
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

question = st.text_input("Ask your fitness question")

if st.button("Ask"):
    if question:
        with st.spinner("Thinking..."):
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=question
            )
        st.write(response.text)
    else:
        st.warning("Please enter a question")import streamlit as st

