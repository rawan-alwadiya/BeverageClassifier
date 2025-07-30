import streamlit as st
import numpy as np
import joblib


scaler = joblib.load("scaler.pkl")
pca = joblib.load("pca.pkl")
model = joblib.load("logistic_regression_model.pkl")


wine_classes = {
    0: "Wine Type 1",
    1: "Wine Type 2",
    2: "Wine Type 3"
}


st.set_page_config(
    page_title="BeverageClassifier",
    page_icon="🍷",
    layout="centered",
    initial_sidebar_state="auto"
)


st.title("🍷 BeverageClassifier")
st.subheader("Predict wine type based on chemical properties")

st.markdown("""
👋 **Welcome!**  
Enter the chemical properties of a wine sample — like alcohol content, acidity, and more — and we'll predict which of **three wine types** it most closely matches.

These wine types come from grape varieties grown in the same region of Italy.
""")


st.markdown("### Input Wine Chemical Properties")

alcohol = st.slider("Alcohol", 11.03, 14.83, 13.00)
malic_acid = st.slider("Malic Acid", 0.74, 5.80, 2.34)
ash = st.slider("Ash", 1.36, 3.23, 2.37)
alcalinity_of_ash = st.slider("Alcalinity of Ash", 10.6, 30.0, 19.49)
magnesium = st.slider("Magnesium", 70.0, 162.0, 99.74)
total_phenols = st.slider("Total Phenols", 0.98, 3.88, 2.30)
flavanoids = st.slider("Flavanoids", 0.34, 5.08, 2.03)
nonflavanoid_phenols = st.slider("Nonflavanoid Phenols", 0.13, 0.66, 0.36)
proanthocyanins = st.slider("Proanthocyanins", 0.41, 3.58, 1.59)
color_intensity = st.slider("Color Intensity", 1.28, 13.0, 5.06)
hue = st.slider("Hue", 0.48, 1.71, 0.96)
od280 = st.slider("OD280/OD315 of diluted wines", 1.27, 4.0, 2.61)
proline = st.slider("Proline", 278.0, 1680.0, 746.89)


if st.button("🔍 Predict Wine Type"):
    user_input = np.array([[alcohol, malic_acid, ash, alcalinity_of_ash, magnesium,
                            total_phenols, flavanoids, nonflavanoid_phenols,
                            proanthocyanins, color_intensity, hue, od280, proline]])

    scaled_input = scaler.transform(user_input)
    pca_input = pca.transform(scaled_input)
    prediction = model.predict(pca_input)[0]

    predicted_class = wine_classes.get(prediction, "Unknown")

    st.success(f"✅ The predicted wine type is: **{predicted_class}**")