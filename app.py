import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="FitBuddy AI", page_icon="💪")
st.title("FitBuddy - AI Fitness Coach")

api_key = st.text_input("Enter Your Friend's Gemini API Key", type="password")

if not api_key:
    st.warning("Paste your friend's API key here")
    st.stop()

genai.configure(api_key=api_key)

age = st.number_input("Age", 15, 80, 20)
weight = st.number_input("Weight (kg)", 30, 150, 60)
height = st.number_input("Height (cm)", 100, 220, 165)
gender = st.selectbox("Gender", ["Female", "Male", "Other"])
goal = st.selectbox("Goal", ["Weight Loss", "Weight Gain", "Muscle Gain", "Stay Fit"])
food = st.selectbox("Food", ["Veg", "Non-Veg", "Veg + Egg"])

if st.button("Generate My Plan"):
    with st.spinner("Generating..."):
        try:
            model = genai.GenerativeModel("gemini-3.8-flash")
            prompt = f"Create Indian diet and workout plan for {age}yr old {gender}, {weight}kg, {height}cm, goal {goal}, food {food}. Give simple points."
            response = model.generate_content(prompt)
            st.success("Your Plan Ready!")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
