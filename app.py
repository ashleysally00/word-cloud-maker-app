import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Streamlit App
st.title("Word Cloud Maker")

st.sidebar.header("Options")
text_input = st.sidebar.text_area("Enter Text", "Type your text here...")
max_words = st.sidebar.slider("Maximum Number of Words", 10, 200, 100)
width = st.sidebar.slider("Width of Word Cloud", 400, 800, 600)
height = st.sidebar.slider("Height of Word Cloud", 400, 800, 400)
background_color = st.sidebar.color_picker("Background Color", "#ffffff")

uploaded_image = st.sidebar.file_uploader("Upload Mask Image (Optional)", type=["png", "jpg", "jpeg"])
mask = None

if uploaded_image:
    image = Image.open(uploaded_image)
    mask = np.array(image)

if st.sidebar.button("Generate Word Cloud"):
    if not text_input.strip():
        st.error("Please enter some text to generate the word cloud!")
    else:
        wordcloud = WordCloud(
            max_words=max_words,
            background_color=background_color,
            width=width,
            height=height,
            mask=mask,
            contour_width=1 if mask is not None else 0,
            contour_color="black" if mask is not None else None,
        ).generate(text_input)

        # Display the word cloud
        st.subheader("Generated Word Cloud")
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation="bilinear")
        ax.axis("off")
        st.pyplot(fig)

st.sidebar.markdown("Made with ❤️ using Streamlit and WordCloud")
