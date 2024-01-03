import pickle
import streamlit as st

model =  pickle.load(open('Estimasi_mobil.sav','rb'))

st.title('Estimasi Harga Mobil Bekas')

year = st.number_input('Input tahun mobil')
mileage = st.number_input('jarak tempuh mobil')
tax = st.number_input('Input pajak mobil')
mpg = st.number_input('input konsumsi BBM Mobil')
engineSize = st.number_input('Input engine Size')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )
    st.write ('Estimasi harga mobil bekas dalam Pounds', predict)
    st.write('Estimasi harga mobil bekas dalam IDR (Juta)', predict*19000)