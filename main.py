import streamlit as st
import functions as ft

ara=st.text_input("Ürün, Marka, Kategori Ara")

if len(ara)>0:
    sonuclar=ft.urunara(ara)
    for sonuc in sonuclar:
        col1,col2,col3=st.columns(3)
        with col1:
            if len(sonuc[5])>0:
                st.image(sonuc[5])
            else:
                st.image("urun.png")
        with col2:
            st.subheader(sonuc[0])
            st.write(sonuc[1])
        with col3:
            st.write("fiyat:",sonuc[4],sonuc[3])

