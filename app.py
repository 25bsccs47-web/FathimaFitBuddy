import streamlit as st
from google import genai

st.set_page_config(page_title="FitBuddy AI", page_icon="💪")
st.title("FitBuddy - AI Fitness Coach")

api_key = st.text_input("Enter Your Gemini API Key", type="password")
if not api_key:
    st.warning("Please enter API Key")
    st.stop()

client = genai.Client(api_key=api_key)

age = st.number_input("Age", 15, 80, 20)
weight = st.number_input("Weight (kg)", 30, 150, 60)
height = st.number_input("Height (cm)", 100, 220, 165)
gender = st.selectbox("Gender", ["Female", "Male", "Other"])
goal = st.selectbox("Goal", ["Weight Loss", "Weight Gain", "Muscle Gain", "Stay Fit"])
food = st.selectbox("Food Preference", ["Veg", "Non-Veg", "Veg + Egg"])

if st.button("Generate My Plan"):
    with st.spinner("Generating..."):
        prompt = f"Create Indian diet and workout plan for {age} year old {gender}, {weight}kg, {height}cm, goal {goal}, food {food}"
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        st.success("Your Plan:")
        st.markdown(response.text)
