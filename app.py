import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="YouTube Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 YouTube Analytics Dashboard")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("youtube_analytics_dataset.csv")

df = load_data()

st.subheader("Dataset")
st.dataframe(df, use_container_width=True)

st.subheader("Informasi Dataset")
col1, col2 = st.columns(2)

with col1:
    st.metric("Jumlah Baris", df.shape[0])

with col2:
    st.metric("Jumlah Kolom", df.shape[1])

st.subheader("Statistik Deskriptif")
st.write(df.describe())

st.subheader("Missing Values")
st.write(df.isnull().sum())

numeric_columns = df.select_dtypes(include="number").columns

if len(numeric_columns) > 0:
    st.subheader("Visualisasi")

    selected_column = st.selectbox(
        "Pilih kolom numerik",
        numeric_columns
    )

    fig, ax = plt.subplots(figsize=(8,4))
    ax.hist(df[selected_column].dropna(), bins=20)
    ax.set_title(f"Histogram {selected_column}")
    ax.set_xlabel(selected_column)
    ax.set_ylabel("Frekuensi")

    st.pyplot(fig)

    st.subheader("Boxplot")

    fig2, ax2 = plt.subplots(figsize=(8,2))
    ax2.boxplot(df[selected_column].dropna(), vert=False)
    ax2.set_title(selected_column)

    st.pyplot(fig2)

st.success("Dashboard berhasil dimuat.")
