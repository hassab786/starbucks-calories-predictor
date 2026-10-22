
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Starbucks Calories Predictor",
    page_icon="☕",
    layout="centered"
)

@st.cache_resource
def load_model():
    return joblib.load("starbucks_model.pkl")

model = load_model()

st.title("☕ Starbucks Nutrition Predictor")
st.write("Enter the drink's nutrition values to estimate its calories.")

st.info(
    "This app predicts calories from nutritional values. "
    "Results are estimates, not official Starbucks nutrition information."
)

with st.form("nutrition_form"):
    st.subheader("Nutrition Information")

    total_fat = st.number_input("Total Fat (g)", min_value=0.0, value=0.1)
    trans_fat = st.number_input("Trans Fat (g)", min_value=0.0, value=0.0)
    saturated_fat = st.number_input("Saturated Fat (g)", min_value=0.0, value=0.0)
    sodium = st.number_input("Sodium (mg)", min_value=0.0, value=0.0)
    carbs = st.number_input("Total Carbohydrates (g)", min_value=0.0, value=10.0)
    cholesterol = st.number_input("Cholesterol (mg)", min_value=0.0, value=0.0)
    fibre = st.number_input("Dietary Fibre (g)", min_value=0.0, value=0.0)
    sugars = st.number_input("Sugars (g)", min_value=0.0, value=0.0)
    protein = st.number_input("Protein (g)", min_value=0.0, value=0.5)
    vitamin_a = st.number_input("Vitamin A (% DV)", min_value=0.0, value=0.0)
    vitamin_c = st.number_input("Vitamin C (% DV)", min_value=0.0, value=0.0)
    calcium = st.number_input("Calcium (% DV)", min_value=0.0, value=0.0)
    iron = st.number_input("Iron (% DV)", min_value=0.0, value=0.0)
    caffeine = st.number_input("Caffeine (mg)", min_value=0.0, value=100.0)

    submitted = st.form_submit_button("Predict Calories")

if submitted:
    input_data = pd.DataFrame([{
        "Total Fat (g)": total_fat,
        "Trans Fat (g)": trans_fat,
        "Saturated Fat (g)": saturated_fat,
        "Sodium (mg)": sodium,
        "Total Carbohydrates (g)": carbs,
        "Cholesterol (mg)": cholesterol,
        "Dietary Fibre (g)": fibre,
        "Sugars (g)": sugars,
        "Protein (g)": protein,
        "Vitamin A (% DV)": vitamin_a,
        "Vitamin C (% DV)": vitamin_c,
        "Calcium (% DV)": calcium,
        "Iron (% DV)": iron,
        "Caffeine (mg)": caffeine
    }])

    prediction = model.predict(input_data)[0]

    st.success(f"Estimated Calories: {prediction:.1f}")
