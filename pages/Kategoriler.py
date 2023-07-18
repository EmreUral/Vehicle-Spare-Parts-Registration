import streamlit as st
import functions as ft

ft.tabloyap("kategoriler","isim TEXT UNIQUE")
with st.form("kategori",clear_on_submit=True):
    isim=st.text_input("Kategori İsmi")
    ekle=st.form_submit_button("Ekle")
    if ekle:
       ft.veriekle("kategoriler",isim)
       st.success("Kategori Eklendi")


ft.tablogetir("kategoriler","id","isim")
