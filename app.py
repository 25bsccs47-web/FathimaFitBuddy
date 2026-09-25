import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Fathima FitBuddy")

st.title("Fathima FitBuddy 💪")

# Configure API
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

question = st.text_input("Enter your question")

if st.button("Ask"):
    if question:
        with st.spinner("Thinking..."):
            response = model.generate_content(question)
        st.write(response.text)
    else:
        st.warning("Please enter a question!")
