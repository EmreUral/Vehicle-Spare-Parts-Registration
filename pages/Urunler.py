import streamlit as st
import functions as ft

modeller=[]
x=ft.verigetir("modeller")

for i in x:
    m=i[1]+" "+i[2]+" "+str(i[3])
    modeller.append(m)

kategoriler=[]
y=ft.verigetir("kategoriler")
for i in y:
    kategoriler.append(i[1])
ft.tabloyap("urunler","isim TEXT,model TEXT,kategori TEXT,kur TEXT,fiyat REAL,resim TEXT,stok INTEGER,orijinal TEXT")
with st.form("model",clear_on_submit=True):
    isim=st.text_input("Ürün İsmi")
    model=st.multiselect("Model Seç",modeller)
    kategori=st.selectbox("Kategori Seç",kategoriler)
    kur=st.selectbox("Fiyat Kuru",["TRY","USD","EUR"])
    fiyat=st.number_input("Fiyat Giriniz")
    resim=st.text_input("Resim URL")
    stok=st.number_input("Stok Giriniz",step=1,value=100)
    orijinal=st.checkbox("Orijinal ürün")
    ekle=st.form_submit_button("Ekle")
    if ekle:
        model2=""
        for m in model:
            model2=model2+m+","
        ft.veriekle("urunler",isim,model2,kategori,kur,fiyat,resim,stok,orijinal)

ft.tablogetir("urunler","id","İsim","Model","Kat","Kur","Fiyat","Resim","Stok","Orijinal")
