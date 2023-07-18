import streamlit as st
import functions as ft

x=ft.verigetir("kategoriler")
kategoriler=[]
for i in x:
    kategoriler.append(i[1])

with st.form("Güncelle",clear_on_submit=True):
    kategori=st.selectbox("Kategori Seç",kategoriler)
    oran=st.number_input("Oran")
    duzenle=st.form_submit_button("Düzenle")
    if duzenle:
        ft.kategorifiyatguncelle(kategori,oran)
        st.success("Fiyat Güncellemesi Başarılı Bir Şekilde Yapıldı")


