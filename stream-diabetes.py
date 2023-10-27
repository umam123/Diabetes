import pickle
import streamlit as st

# membaca model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

#judul web
st.markdown("# <center>Diabetes Predictor</center>", unsafe_allow_html=True)

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    Pregnancies = st.text_input ('Pregnancies', min_value=0, max_value=9)

with col2 :
    Glucose = st.text_input ('Glucose', min_value=0)

with col1 :
    BloodPressure = st.text_input ('Blood Pressure', min_value=0)

with col2 :
    SkinThickness = st.text_input ('Skin Thickness', min_value=0)

with col1 :
    Insulin = st.text_input ('Insulin', min_value=0)

with col2 :
    BMI = st.text_input ('BMI', min_value=0.01)

with col1 :
    DiabetesPedigreeFunction = st.text_input ('Diabetes Pedigree Function', min_value=0.001)

with col2 :
    Age = st.text_input ('Age', min_value=0)

# code untuk prediksi
diab_diagnosis = ''


# membuat tombol untuk prediksi
if st.button('Predict'):
    data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]).reshape(1, -1)
    diab_prediction = diabetes_model.predict(data)

    if diab_prediction[0] == 1:
        st.write("The model predicts that you have diabetes.")
    else:
        st.write("The model predicts that you don't have diabetes.")
