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
# code untuk prediksi
diab_diagnosis = ''

# Use HTML and CSS to center the button
st.markdown(
    """
    <div style="display: flex; justify-content: center; align-items: center;">
        <button style="padding: 10px 20px;" id="predict-button">Predict</button>
    </div>
    """,
    unsafe_allow_html=True,
)

# JavaScript to trigger the prediction on button click
st.markdown(
    """
    <script>
        document.getElementById("predict-button").onclick = function() {
            var input_data = "Replace with your input data";  // You can get input data from a Streamlit widget
            var data = JSON.parse(input_data);
            var diab_prediction = diabetes_model.predict(data);

            if (diab_prediction[0] === 1) {
                alert("The model predicts that you have diabetes.");
            } else {
                alert("The model predicts that you don't have diabetes.");
            }
        }
    </script>
    """,
    unsafe_allow_html=True,
)
