import streamlit as st
import eda
import predict

page = st.sidebar.selectbox('Pilih Halaman: ', ('Prediction', 'EDA'))

if page == 'EDA':
    eda.run()
else:
    predict.run()