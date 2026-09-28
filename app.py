import streamlit as st
from google import genai

st.set_page_config(page_title="FitBuddy AI", page_icon="💪")
st.title("FitBuddy - AI Fitness Coach")
st.write("Personal AI Diet and Workout Planner")

# FIXED: Only use text input, no secrets
api_key = st.text_input("Enter Your Gemini API Key", type="password")

if not api_key:
    st.warning("Please enter API Key from aistudio.google.com/app/apikey")
    st.stop()

client = genai.Client(api_key=api_key)

st.subheader("Enter Your Details")
col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Age", 15, 80, 20)
    weight = st.number_input("Weight (kg)", 30, 150, 60)
with col2:
    height = st.number_input("Height (cm)", 100, 220, 165)
    gender = st.selectbox("Gender", ["Female", "Male", "Other"])

goal = st.selectbox("Goal", ["Weight Loss", "Weight Gain", "Muscle Gain", "Stay Fit"])
food = st.selectbox("Food Preference", ["Veg", "Non-Veg", "Veg + Egg"])
level = st.selectbox("Activity Level", ["Beginner", "Intermediate", "Advanced"])

if st.button("Generate My Plan"):
    with st.spinner("Generating your plan..."):
        prompt = f"Act as an expert Indian fitness coach. User details: {age} years old {gender}, {weight}kg, {height}cm. Goal is {goal}, Food preference is {food}, Level is {level}. Give detailed Indian diet and workout plan."
        
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            st.success("Your Plan is Ready!")
            st.markdown(response.text)
        except Exception as e:
            try:
                st.error(f"Trying with fallback model... Error was: {e}")
                response = client.models.generate_content(
                    model="gemini-1.5-flash",
                    contents=prompt
                )
                st.success("Your Plan is Ready!")
                st.markdown(response.text)
            except Exception as e2:
                st.error(f"Final Error: {e2}")
