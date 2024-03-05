import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Proyek Akhir Analisis Data")
st.write(
    """
    - **Nama:** Aikal Ichsan Alqadri
    - **Email:** aikalichsan2@gmail.com
    - **ID Dicoding:** aikal_ichsan_GPyH
    """
)

all_df = pd.read_csv("main_data.csv")

st.subheader("Geoanalysis")
col1, col2, = st.columns(2)

with col1:
    daySum = all_df.groupby("weathersit")["cnt_x"].sum()
    st.write("Jumlah Sepeda Disewa (Harian) pada Kondisi Cuaca yang Berbeda", daySum)

with col2:
    hourSum = all_df.groupby("weathersit")["cnt_y"].sum()
    st.write("Jumlah Sepeda Disewa (Jam) pada Kondisi Cuaca yang Berbeda", hourSum)

col1, col2, = st.columns(2)
daySum = all_df.groupby("weathersit")["cnt_x"].sum().reset_index()
hourSum = all_df.groupby("weathersit")["cnt_y"].sum().reset_index()

with col1:
    plt.figure(figsize=(10, 6))
    plt.bar(["Cerah", "Berawan/Berkabut", "Hujan/Salju Ringan", "Hujan Deras/Salju Lebat"], daySum['cnt_x'], color="paleturquoise")
    plt.title("Jumlah Sepeda Disewa (Harian) pada Kondisi Cuaca yang Berbeda")
    plt.xlabel("Kondisi Cuaca")
    plt.ylabel("Jumlah")
    plt.tick_params(axis='x', rotation=30)
    st.pyplot(plt)

with col2:
    plt.figure(figsize=(10, 6))
    plt.bar(["Cerah", "Berawan/Berkabut", "Hujan/Salju Ringan", "Hujan Deras/Salju Lebat"], hourSum['cnt_y'], color="lightcoral")
    plt.title("Jumlah Sepeda Disewa (Jam) pada Kondisi Cuaca yang Berbeda")
    plt.xlabel("Kondisi Cuaca")
    plt.ylabel("Jumlah")
    plt.tick_params(axis='x', rotation=30)
    st.pyplot(plt)

st.write(
    """
    Berikut adalah hasil visualisasi dari geoanalysis berapa banyaknya sepeda disewa pada kondisi cuaca yang berbeda. 
    **Tetapi, dikarenakan ada bar yang tidak terlihat karena nilainya terlalu kecil**, maka garis y akan diskalakan dengan logaritma agar terlihat.
    """
)

col1, col2, = st.columns(2)
daySum = all_df.groupby("weathersit")["cnt_x"].sum().reset_index()
hourSum = all_df.groupby("weathersit")["cnt_y"].sum().reset_index()

with col1:
    plt.figure(figsize=(10, 6))
    plt.bar(["Cerah", "Berawan/Berkabut", "Hujan/Salju Ringan", "Hujan Deras/Salju Lebat"], daySum['cnt_x'], color="paleturquoise")
    plt.title("Jumlah Sepeda Disewa (Harian) pada Kondisi Cuaca yang Berbeda (Log)")
    plt.xlabel("Kondisi Cuaca")
    plt.ylabel("Jumlah")
    plt.yscale("log")
    plt.tick_params(axis='x', rotation=30)
    st.pyplot(plt)

with col2:
    plt.figure(figsize=(10, 6))
    plt.bar(["Cerah", "Berawan/Berkabut", "Hujan/Salju Ringan", "Hujan Deras/Salju Lebat"], hourSum['cnt_y'], color="lightcoral")
    plt.title("Jumlah Sepeda Disewa (Jam) pada Kondisi Cuaca yang Berbeda (Log)")
    plt.xlabel("Kondisi Cuaca")
    plt.ylabel("Jumlah")
    plt.yscale("log")
    plt.tick_params(axis='x', rotation=30)
    st.pyplot(plt)

st.write(
    """
    Sepeda paling banyak disewa saat keadaan Cerah sebesar 2257952 pada harian dan 2338173 pada setiap jam. 
    Sedangkan sepeda paling sedikit disewa saat keadaan Hujan Deras/Salju Lebat sebesar 0 pada harian dan 223 pada setiap jamnya.
    """
)

st.subheader("Pertanyaan 1")
st.write(
    """
    - Pada bulan apa jasa rental sepeda paling banyak dan paling sedikit tersewa?
    """
)

monthly = all_df.groupby("mnth")["cnt_x"].sum().reset_index()

plt.figure(figsize=(10, 6))
plt.bar(monthly["mnth"], monthly["cnt_x"], color='sandybrown')

plt.xlabel("Bulan")
plt.ylabel("Jumlah")
plt.title("Jumlah Rental per Bulan")
plt.grid(axis="y")
st.pyplot(plt)

st.write(
    """
    Berdasarkan bar plot diatas, kita dapat melihat secara visual jumlah rental sepeda per bulannya. 
    Rata-rata perentalan perbulannya adalah 274389, paling banyaknya adalah 351194 dan paling sedikitnya adalah 134933.
    """
)

st.subheader("Pertanyaan 2")
st.write(
    """
    - Bagaimana perbandingan jumlah pengguna kasual dan pengguna yang mendaftar per jamnya?
    """
)

plt.figure(figsize=(10, 6))
bar_width = 0.35

plt.bar(all_df["hr"] - bar_width/2, all_df["casual_y"], bar_width, label="Casual")
plt.bar(all_df["hr"] + bar_width/2, all_df["registered_y"], bar_width, label="Registered")

plt.xlabel("Jam")
plt.ylabel("Jumlah")
plt.title("Jumlah Casual dan Registered per Jam")
plt.legend()
plt.grid(True)
st.pyplot(plt)

st.write(
    """
    Berdasarkan bar plot diatas, kita dapat melihat secara visual jumlah casual dan registered per jamnya. 
    Rata-rata perjamnya untuk casual adalah 35.676218, untuk registerednya adalah 153.786869. 
    Paling banyak untuk casualnya adalah 367 dan yang paling banyak untuk registered adalah 886.
    """
)
