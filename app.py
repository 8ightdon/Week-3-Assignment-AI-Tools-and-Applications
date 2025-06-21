
import streamlit as st
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

@st.cache_resource
def load_model():
    model = tf.keras.models.load_model('mnist_cnn_model.h5')
    return model

model = load_model()

st.title("MNIST Digit Recognizer")
st.write("Upload a 28x28 grayscale image of a handwritten digit.")

uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('L').resize((28, 28))
    img_array = np.array(image)
    st.image(image, caption='Uploaded Image', width=150)

    img_input = img_array.reshape(1, 28, 28, 1) / 255.0
    prediction = model.predict(img_input)
    pred_label = np.argmax(prediction)

    st.write(f"### Predicted Digit: {pred_label}")
    st.bar_chart(prediction[0])
