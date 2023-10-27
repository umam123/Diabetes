# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Iumj17F8acb7oCk5gyDuK5UZ-h-huitF
"""

import streamlit as st
import pickle
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

from sklearn.model_selection import GridSearchCV

# Load the trained model
with open('KNN_pickel.sav', 'rb') as file:
    
    model = pickle.load(file)

st.title("Diabetes Predictor")

melahirkan = st.number_input("Pregnancies", min_value=0, max_value=9)
glukosa = st.number_input("Glucose", min_value=0)
darah = st.number_input("BloodPressure", min_value=0)
kulit = st.number_input("SkinThickness", min_value=0)
insulin = st.number_input("Insulin", min_value=0)
bmi = st.number_input("BMI", min_value=0.001)
riwayat = st.number_input("DiabetesPedigreeFunction", min_value=0.001)
umur = st.number_input("Age", min_value=0)

st.text("Enter your data and click the 'Predict' button to see the result.")
if st.button("Predict"):
    data = np.array([melahirkan, glukosa, darah, kulit, insulin, bmi, riwayat, umur]).reshape(1, -1)
    isDiabetes = model.predict(data)

    if isDiabetes[0] == 1:
        st.write("The model predicts that you have diabetes.")
    else:
        st.write("The model predicts that you don't have diabetes.")


