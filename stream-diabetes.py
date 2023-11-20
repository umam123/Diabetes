from datetime import datetime
import pandas as pd
import pickle
import streamlit as st
import numpy as np
from streamlit_gsheets import GSheetsConnection

# Establishing a Google Sheets connection
conn = st.experimental_connection("gsheets", type=GSheetsConnection)
# Fetch existing vendors data
existing_data = conn.read(worksheet="DataDiabetes", usecols=list(range(6)), ttl=5)
existing_data = existing_data.dropna(how="all")

# membaca model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
font_size = 14  
#judul web
st.markdown("# <center>Diabetes Predictor</center>", unsafe_allow_html=True)

#membagi kolom
col1, col2 = st.columns(2)
with col1 :
    Name = st.text_input(label="Name*")
with col2 :
    Birth_Day = st.date_input(label="Birht Day*")
with col1 :
    Country = st.text_input(label="Country*")
with col2 :
    City = st.text_input(label="City*")
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
st.markdown("**required*")
#membagi kolom
col1, col2, col3, col4, col5 = st.columns(5)
# membuat tombol untuk prediksi
with col2 :
    if st.button("Predict"):
        data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]).reshape(1, -1)
        Prediction = diabetes_model.predict("Prediction",data)
        if Prediction[0] == 1:
            st.markdown(f"<h1 style='text-align: center; font-size: {font_size}px;'>The model predicts that you have diabetes.</h1>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h1 style='text-align: center; font-size: {font_size}px;'>The model predicts that you don't have diabetes.</h1>", unsafe_allow_html=True)
with col4 :
    
    if st.button("Save"):
            if not Name or not Birth_Day:
                st.warning("Ensure all mandatory fields are filled.")
               
            else:
                # Creating updated data entry
                updated_diabetes_data = pd.DataFrame(
                    [
                        {
                            "Name": Name,
                            "Birth Day": Birth_Day.strftime("%Y-%m-%d"),
                            "Pregnancies": Pregnancies,
                            "Glucose" : Glucose,
                            "Blood Pressure" : BloodPressure,
                            "Skin Thickness" : SkinThickness,
                            "Insulin" : Insulin,
                            "BMI" : BMI,
                            "Diabetes Pedigree Function (DPF)" : DiabetesPedigreeFunction,
                            "Age" : Age,
                            "Country" : Country,
                            "City" : City,
                            "Prediction" : Prediction,
                            
                        }
                    ]
                )
                # Adding updated data to the dataframe
                updated_df = pd.concat([existing_data, updated_diabetes_data], ignore_index=True)
                # Update google sheet the new diabetes data
                conn.update(worksheet="DataDiabetes", data=updated_df)
                st.success("Data Save")
