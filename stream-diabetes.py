import pickle
import streamlit as st
import numpy as np


# membaca model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

#judul web
st.markdown("# <center>Diabetes Predictor</center>", unsafe_allow_html=True)

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    Pregnancies = st.number_input ("Pregnancies", min_value=0, max_value=9)

with col2 :
    Glucose = st.number_input ("Glucose", min_value=0)

with col1 :
    BloodPressure = st.number_input ("Blood Pressure", min_value=0)

with col2 :
    SkinThickness = st.number_input ("Skin Thickness", min_value=0)

with col1 :
    Insulin = st.number_input ("Insulin", min_value=0)

with col2 :
    BMI = st.number_input ("BMI", min_value=0.01)

with col1 :
    DiabetesPedigreeFunction = st.number_input ("Diabetes Pedigree Function (DPF)", min_value=0.001)

with col2 :
    Age = st.number_input ("Age", min_value=0)

st.text("DPF = Number of family with diabetes/Total of family member")

#membagi kolom
col1, col2, col3 = st.columns(3)
# membuat tombol untuk prediksi
with col2 :
    if st.button("# <center>Predict</center>", unsafe_allow_html=True):
        data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]).reshape(1, -1)
        diab_prediction = diabetes_model.predict(data)

        if diab_prediction[0] == 1:
            st.write("The model predicts that you have diabetes.")
        else:
            st.write("The model predicts that you don't have diabetes.")
