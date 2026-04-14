import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("Wine Quality.pkl", "rb"))

# Page config
st.set_page_config(page_title="Wine Quality Predictor", layout="wide")

# Title
st.markdown("<h1 style='text-align: center;'>Wine Quality Prediction 🍷</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter wine chemical properties to predict quality</p>", unsafe_allow_html=True)

st.divider()

# Layout: 2 columns
col1, col2 = st.columns(2)

# LEFT COLUMN
with col1:
    st.subheader("🧪 Chemical Properties")

    fixed_acidity = st.text_input("Fixed Acidity", "8.1")
    volatile_acidity = st.text_input("Volatile Acidity", "0.38")
    citric_acid = st.text_input("Citric Acid", "0.28")
    residual_sugar = st.text_input("Residual Sugar", "2.1")
    chlorides = st.text_input("Chlorides", "0.066")

# RIGHT COLUMN
with col2:
    st.subheader("⚗️ Additional Features")

    free_sulfur_dioxide = st.text_input("Free Sulfur Dioxide", "13")
    total_sulfur_dioxide = st.text_input("Total Sulfur Dioxide", "30")
    density = st.text_input("Density", "0.9968")
    pH = st.text_input("pH", "3.23")
    sulphates = st.text_input("Sulphates", "0.73")
    alcohol = st.text_input("Alcohol", "9.7")

st.divider()

# Prediction button centered
col_center = st.columns([1,2,1])[1]

with col_center:
    predict_btn = st.button("🔍 Predict Quality", use_container_width=True)

# Prediction Logic
if predict_btn:
    try:
        input_data = np.array([[float(fixed_acidity), float(volatile_acidity), float(citric_acid),
                                float(residual_sugar), float(chlorides), float(free_sulfur_dioxide),
                                float(total_sulfur_dioxide), float(density), float(pH),
                                float(sulphates), float(alcohol)]])

        prediction = model.predict(input_data)

        st.divider()

        # Result UI
        if prediction[0] == 1:
            st.markdown(
                "<h2 style='text-align:center; color:green;'>Good Quality Wine.Enjoy Cheers🍷!</h2>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                "<h2 style='text-align:center; color:red;'>⚠️ Bad Quality Wine.Be Carefull!</h2>",
                unsafe_allow_html=True
            )

        # Debug (optional)
        with st.expander("See Input Data"):
            st.write(input_data)

    except:
        st.error("⚠️ Please enter valid numeric values")

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center;'>Built with Streamlit 🚀</p>", unsafe_allow_html=True)