import streamlit as st
import functions as ft

x=ft.verigetir("urunler")
urunler=[]
for i in x:
    urunler.append(i[1])

with st.form("Ürün Sil",clear_on_submit=True):
    liste=st.multiselect("Sileceğiniz Ürünleri Seçin",urunler)
    sil=st.form_submit_button("Ürünleri Sil")
    if sil:
        sonuc=ft.urunsil(liste)
        st.success(sonuc)

