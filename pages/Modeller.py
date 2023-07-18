import streamlit as st
import functions as ft

markalar=[]
x=ft.verigetir("Markalar")
for i in x:
    markalar.append(i[1])

ft.tabloyap("modeller","marka TEXT,isim TEXT,yil İNTEGER,resim TEXT")

with st.form("Model Ekle"):
    marka=st.selectbox("Marka Seç",markalar)
    isim=st.text_input("Model İsim")
    yil=st.selectbox("Model Yılı",range(1940,2024))
    resim=st.text_input("Model Resim URL")
    ekle=st.form_submit_button("Model Ekle")
    if ekle:
        ft.veriekle("modeller",marka,isim,yil,resim)

ft.tablogetir("modeller","id","marka","model","yil","resim")

