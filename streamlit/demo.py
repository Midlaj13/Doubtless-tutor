import streamlit as st
import openai
from PIL import Image

# Set your OpenAI API key here
openai.api_key = "YOUR_OPENAI_API_KEY"

# Streamlit app layout
st.title("ChatGPT Clone with Text and Image Input")
st.write("Enter a message and upload an image, and get a response from ChatGPT!")

# Text input from the user
user_input = st.text_input("You:", "")

# Image upload
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# Generate response using GPT-3.5
if user_input or uploaded_image:
    prompt = user_input
    if uploaded_image:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        # You can perform further image processing here if needed
        prompt += f"\nImage: {uploaded_image.name}"

    if prompt:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=50
        )
        bot_response = response.choices[0].text.strip()
        st.text("ChatGPT:")
        st.write(bot_response)
