import streamlit as st
import functions as ft
import pandas as pd

st.title("Markalar")

ft.tabloyap("Markalar", "isim TEXT,iskonto REAL")
with st.form("marka", clear_on_submit=True):
    isim = st.text_input("Marka İsim")
    isim = isim.lower()
    iskonto = st.number_input("İskonto Oranı")
    st.warning("İskonto oranı 0 ile 1 arasında olmalıdır örneğin 0.3 %30 indirim")
    ekle = st.form_submit_button("Marka Ekle")
    if ekle:
        ft.veriekle("Markalar", isim, iskonto)
        st.success("Marka Eklendi.")


ft.tablogetir("Markalar","id","marka","iskonto")
