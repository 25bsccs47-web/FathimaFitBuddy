import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="FitBuddy AI")

try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
except:
    st.error("API Key not found! Add it in Streamlit Secrets.")
    st.stop()

st.title("FitBuddy - Your AI Fitness Assistant")
st.write("Ask me anything about diet, workout, and weight loss!")

user_question = st.text_input("What is your question?")

if st.button("Ask"):
    if user_question:
        with st.spinner("Thinking..."):
            prompt = f"You are a helpful fitness trainer. Answer clearly: {user_question}"
            response = model.generate_content(prompt)
            st.success(response.text)
    else:
        st.warning("Please enter a question!")
