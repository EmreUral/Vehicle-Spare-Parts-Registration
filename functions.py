import sqlite3
import pandas as pd
import streamlit as st

conn=sqlite3.connect("stok.sqlite3")
c=conn.cursor()

def tabloyap(isim,sutunlar):
    conn=sqlite3.connect("stok.sqlite3")
    c=conn.cursor()
    komut=f"CREATE TABLE IF NOT EXISTS {isim}({sutunlar})"
    c.execute(komut)
    conn.commit()

def veriekle(isim,*veriler):
    conn=sqlite3.connect("stok.sqlite3")
    c=conn.cursor()
    if len(veriler)==1:
        komut=f"INSERT INTO {isim} VALUES('{veriler[0]}')"
    else:
        komut=f"INSERT INTO {isim} VALUES{veriler}"
    c.execute(komut)
    conn.commit()

def verigetir(isim):
    conn=sqlite3.connect("stok.sqlite3")
    c=conn.cursor()
    komut=f"SELECT rowid,* FROM {isim}"
    c.execute(komut)
    sonuc=c.fetchall()
    return sonuc

def tablogetir(isim,*sutunlar):
    sonuc=verigetir(isim)
    tablo=pd.DataFrame(sonuc)
    tablo.columns=sutunlar
    st.table(tablo)

def urunara(sorgu):
    conn = sqlite3.connect("stok.sqlite3")
    c = conn.cursor()
    komut=f"SELECT * FROM urunler WHERE isim LIKE '%{sorgu}%' OR model LIKE '%{sorgu}%' OR kategori LIKE '%{sorgu}%' "
    c.execute(komut)
    sonuc=c.fetchall()
    return sonuc

def kategorifiyatguncelle(kategori,oran):
    conn = sqlite3.connect("stok.sqlite3")
    c = conn.cursor()
    oran=oran+1
    komut=f"UPDATE urunler SET fiyat=fiyat*{oran} WHERE kategori='{kategori}'"
    c.execute(komut)
    conn.commit()

def urunsil(urunler):
    for urun in urunler:
        adet=len(urunler)
        conn = sqlite3.connect("stok.sqlite3")
        c = conn.cursor()
        komut=f"DELETE FROM urunler WHERE isim='{urun}'"
        c.execute(komut)
        conn.commit()
        mesaj=str(adet)+"Adet Ürün Silindi"
    return mesaj




