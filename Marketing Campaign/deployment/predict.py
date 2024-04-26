import streamlit as st
import pandas as pd
import pickle

# Load the pre-trained model using pickle
def run():
    with open('model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    # Create a Streamlit web app
    st.title("Prediksi Kemampuan Bayar")

    # Add input fields for user input
    st.sidebar.header("Historis Pembayaran")

    pay_status_sept = st.sidebar.slider("pay_0 (Pembayaran status in September, 2005)", -2, 8, 0)
    pay_status_aug = st.sidebar.slider("pay_2 (Pembayaran status in August, 2005)", -2, 8, 0)
    pay_status_jul = st.sidebar.slider("pay_3 (Pembayaran status in July, 2005)", -2, 8, 0)
    pay_status_jun = st.sidebar.slider("pay_4 (Pembayaran status in June, 2005)", -2, 8, 0)
    pay_status_may = st.sidebar.slider("pay_5 (Pembayaran status in May, 2005)", -2, 8, 0)
    pay_status_apr = st.sidebar.slider("pay_6 (Pembayaran status in April, 2005)", -2, 8, 0)

    user_input_data = pd.DataFrame({
        "pay_0": [pay_status_sept],
        "pay_2": [pay_status_aug],
        "pay_3": [pay_status_jul],
        "pay_4": [pay_status_jun],
        "pay_5": [pay_status_may],
        "pay_6": [pay_status_apr],
    })

    # Predict button
    if st.sidebar.button("Hitung"):
        # Make predictions using the loaded model
        predicted_default = model.predict(user_input_data)

        # Display the prediction result
        st.subheader("Hasil Prediksi")
        if predicted_default[0] == 1:
            st.write("Debitur diprediksi akan gagal bayar tagihan di bulan depan.")
        else:
            st.write("Debitur diprediksi mampu membayar tagihan di bulan depan.")