import streamlit as st
import pickle
import numpy as np


# Load the trained model
model = pickle.load(open('modeldiabetes.sav'))



st.title("Diabetes Predictor")
# Membagi Kolom
col1, col2 = st.columns (2)
with col1 :
    melahirkan = st.number_input("Pregnancies", min_value=0, max_value=9)
with col2 :
    glukosa = st.number_input("Glucose", min_value=0)
with col1 :
    darah = st.number_input("BloodPressure", min_value=0)
with col2 :
    kulit = st.number_input("SkinThickness", min_value=0)
with col1 :
    insulin = st.number_input("Insulin", min_value=0)
with col2 :
    bmi = st.number_input("BMI", min_value=0.001)
with col1 :
    riwayat = st.number_input("DiabetesPedigreeFunction", min_value=0.001)
with col2 :
    umur = st.number_input("Age", min_value=0)

st.text("Enter your data and click the 'Predict' button to see the result.")
if st.button("Predict"):
    data = np.array([melahirkan, glukosa, darah, kulit, insulin, bmi, riwayat, Age]).reshape(1, -1)
    isDiabetes = model.predict(data)

    if isDiabetes[0] == 1:
        st.write("The model predicts that you have diabetes.")
    else:
        st.write("The model predicts that you don't have diabetes.")


