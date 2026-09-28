import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="FitBuddy AI", page_icon="💪")
st.title("FitBuddy - AI Fitness Coach")
st.write("Personal AI Diet and Workout Planner")

# Get API Key
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except:
    api_key = st.text_input("Enter Your Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    st.subheader("Enter Your Details")
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", 15, 80, 20)
        weight = st.number_input("Weight (kg)", 30, 150, 60)
    with col2:
        height = st.number_input("Height (cm)", 100, 220, 165)
        gender = st.selectbox("Gender", ["Female", "Male", "Other"])

    goal = st.selectbox("Select Your Goal", ["Weight Loss", "Weight Gain", "Muscle Gain", "Stay Fit"])
    food = st.selectbox("Food Preference", ["Veg", "Non-Veg", "Veg + Egg"])
    level = st.selectbox("Activity Level", ["Beginner", "Intermediate", "Advanced"])

    if st.button("Generate My Plan"):
        with st.spinner("Generating your plan..."):
            try:
                prompt = f"""
                Act as an Indian fitness coach.
                User: {age} years old {gender}, {weight}kg, {height}cm, Goal is {goal}, 
                Food Type is {food}, Fitness Level is {level}.
                Provide:
                1. A 7-Day Indian {food} Diet Plan in a table format with calories
                2. A 7-Day Home Workout Plan
                3. 3 Health Tips
                Keep it simple and easy to follow.
                """
                response = model.generate_content(prompt)
                st.success("Your Plan is Ready!")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error occurred: {e}")
else:
    st.warning("Please enter API Key to continue. Get it from aistudio.google.com/app/apikey")

st.markdown("---")
st.caption("Made for FitBuddy Project")
