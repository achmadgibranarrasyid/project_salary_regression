# app.py
import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("model/salary_model.pkl", "rb"))

# UI Streamlit
st.title("Prediksi Gaji Berdasarkan Pengalaman Kerja")
st.write("Aplikasi ini memprediksi gaji seseorang berdasarkan tahun pengalaman kerja.")

# Input user
years_exp = st.number_input("Masukkan tahun pengalaman kerja:", min_value=0.0, step=0.5)

if st.button("Prediksi Gaji"):
    prediction = model.predict(np.array([[years_exp]]))[0]
    st.success(f"Estimasi Gaji: Rp {prediction:,.2f}")
