import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# Load data
df = pd.read_csv("ProyekAnalisisDataBike.csv")

# Convert date column to datetime
df['dteday'] = pd.to_datetime(df['dteday'])

# Sidebar untuk memilih bulan
with st.sidebar:
    selected_month = st.selectbox('Pilih Bulan', df['month'].unique())
    filtered_month_df = df[df['month'] == selected_month]

# Plot pengaruh hari kerja terhadap jumlah penyewaan sepeda di bulan tertentu
st.header('Pengaruh Hari Kerja Terhadap Jumlah Penyewaan Sepeda di Bulan Tertentu')
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x='workingday', y='cnt', data=filtered_month_df, palette='Set2', ci=None, ax=ax)
ax.set_title('Pengaruh Hari Kerja Terhadap Jumlah Penyewaan Sepeda di Bulan Tertentu')
ax.set_xlabel('Hari Kerja (1=Hari Kerja, 0=Libur)')
ax.set_ylabel('Jumlah Penyewaan Sepeda')
ax.set_xticklabels(['Hari Libur', 'Hari Kerja'])
st.pyplot(fig)

# Plot tren penyewaan sepeda berdasarkan hari dalam seminggu dan hari kerja/libur
st.header('Jumlah Penyewaan Sepeda Berdasarkan Hari dalam Seminggu dan Hari Kerja/Libur')
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=filtered_month_df, x='weekday', y='cnt', hue='workingday', palette='Set1', ci=None, ax=ax)
ax.set_title('Jumlah Penyewaan Sepeda Berdasarkan Hari dalam Seminggu dan Hari Kerja/Libur')
ax.set_xlabel('Hari dalam Seminggu')
ax.set_ylabel('Jumlah Penyewaan Sepeda')
ax.legend(title='Hari Kerja/Libur', labels=['Hari Libur', 'Hari Kerja'])
ax.set_xticklabels(['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'])
st.pyplot(fig)

# Menghitung rata-rata penyewaan sepeda untuk hari kerja dan libur
avg_workingday = filtered_month_df[filtered_month_df['workingday'] == 1]['cnt'].mean()
avg_weekend = filtered_month_df[filtered_month_df['workingday'] == 0]['cnt'].mean()

# Menampilkan rata-rata penyewaan sepeda untuk hari kerja dan hari libur
st.write(f'Rata-rata penyewaan sepeda pada hari kerja: {avg_workingday}')
st.write(f'Rata-rata penyewaan sepeda pada hari libur: {avg_weekend}')

# Plot jumlah penyewaan sepeda berdasarkan musim dan bulan
st.header('Jumlah Penyewaan Sepeda Berdasarkan Musim dan Bulan (Bar Chart)')
fig, ax = plt.subplots(figsize=(16, 8))
sns.barplot(data=df, x='month', y='cnt', hue='season', palette='Set1', ci=None, ax=ax)
ax.set_title('Jumlah Penyewaan Sepeda Berdasarkan Musim dan Bulan (Bar Chart)')
ax.set_xlabel('Bulan')
ax.set_ylabel('Jumlah Penyewaan Sepeda')
ax.legend(title='Musim', labels=['Spring (Merah)', 'Summer (Hijau)', 'Fall (Biru)', 'Winter (Ungu)'])
st.pyplot(fig)