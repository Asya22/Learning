import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import streamlit as st

# Judul Aplikasi
st.title("Analisis Data Peminjaman Sepeda")

# Membaca Data
df = pd.read_csv('day.csv')

# Menampilkan Data
st.subheader("Dataframe")
st.write(df.head())

# Menentukan Statistik Dasar
st.subheader("Statistik Deskriptif")
st.write(df.describe())

# Visualisasi Pertanyaan 1
st.subheader("Jumlah Peminjaman Sepeda Berdasarkan Hari Libur")
fig, ax = plt.subplots()
sns.barplot(x='holiday', y='cnt', data=df, ax=ax)
ax.set_xticklabels(['Hari Kerja', 'Hari Libur'])
ax.set_xlabel('Holiday')
ax.set_ylabel('Jumlah Peminjaman')
st.pyplot(fig)

# Visualisasi Pertanyaan 2
st.subheader("Jumlah Peminjaman Berdasarkan Kondisi Cuaca")
fig2, ax2 = plt.subplots()
sns.barplot(x='weathersit', y='cnt', data=df, ax=ax2)
ax2.set_xticklabels(['Cerah', 'Berawan', 'Gerimis', 'Hujan Lebat'])
ax2.set_xlabel('Kondisi Cuaca')
ax2.set_ylabel('Jumlah Peminjaman')
st.pyplot(fig2)

# Clustering
st.subheader("Analisis Clustering")
features = ['cnt', 'holiday']
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df[features])
kmeans = KMeans(n_clusters=2, random_state=42)
df['cluster'] = kmeans.fit_predict(scaled_data)

fig3, ax3 = plt.subplots()
sns.boxplot(x='holiday', y='cnt', hue='cluster', data=df, ax=ax3)
ax3.set_xticklabels(['Hari Kerja', 'Hari Libur'])
ax3.set_title('Cluster Analysis by Holiday and Count')
st.pyplot(fig3)
