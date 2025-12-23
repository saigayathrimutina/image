import streamlit as st
import random

st.title("🎨 AI Text-to-Image Generator (Demo)")

# Initialize session state for prompt
if "prompt" not in st.session_state:
    st.session_state.prompt = ""

# Function for Surprise Me button
def surprise_me():
    st.session_state.prompt = random.choice([
        "Cyberpunk city at night",
        "Astronaut riding a horse",
        "AI robot painting art",
        "Futuristic Indian village",
        "Flying cars in the future"
    ])

# Text input
st.text_input("Describe the image you want...", key="prompt")

# Style selection
style = st.selectbox("Select Style", ["Realistic", "Anime", "3D", "Digital Art"])

# Surprise Me button
if st.button("🎲 Surprise Me"):
    surprise_me()

# Generate button (Demo)
if st.button("✨ Generate Image"):
    if st.session_state.prompt.strip() == "":
        st.warning("Please enter a prompt!")
    else:
        # Instead of calling API, show a placeholder image
        st.image(
            "https://via.placeholder.com/512x512.png?text=AI+Image+Demo",
            caption=f"Demo Image for: {style} style, '{st.session_state.prompt}'",
            use_column_width=True
        )
        st.success("This is a demo. No API key is needed!")
