import streamlit as st

st.set_page_config(page_title="Growth Mindset Project", page_icon="✥")
st.title("Growth Mindset AI With Streamlit")

st.header("Welcome To your Growth Journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This AI-powered app helps you build a growth mindset with reflection, challenges, and achievements!")

st.header("Today's Growth Mindset")
st.write("Success is not final, failure is not fatal: it is the courage to continue that counts!")

st.header("What's your Challenge Today?")
user_input = st.text_input("Describe a challenge you are facing:")

if user_input:
    st.success(f"You are facing: {user_input}. Keep pushing forward towards your goal!")
else:
    st.warning("Tell us about your Challenge to get started!")

st.header("Reflection on your Learning")
reflection = st.text_area("Write your outcome here:")

if reflection:
    st.success(f"Great Insight! Your Reflection: {reflection}")
else:
    st.info("Reflecting on past experiences helps you grow! Share your difficulties.")

st.header("Celebrate your Achievements")
achievements = st.text_input("Share something you've recently accomplished:")

if achievements:
    st.success(f"Amazing! You achieved: {achievements}")     
else:
    st.info("Big or small, every achievement counts! Share one now!")

st.write("- - -")    
st.write("Keep believing in yourself. Growth is a journey, not a destination.")
st.write("Created by Hafsa Sultan")
