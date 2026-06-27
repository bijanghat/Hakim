import streamlit as st
import pandas as pd

# Konfigurasi halaman
st.set_page_config(
    page_title="YouTube Analytics Dashboard",
    page_icon="📊",
    layout="wide" )


# Judul
st.title("📊 YouTube Analytics Dashboard")
st.markdown("Dashboard sederhana untuk analisis dataset YouTube.")

# Membaca dataset
@st.cache_data
def load_data():
    return pd.read_csv("youtube_analytics_dataset.csv")

try:
    df = load_data()

    st.success("✅ Dataset berhasil dimuat!")

    # ==========================
    # KPI
    # ==========================
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📄 Total Data", len(df))

    with col2:
        st.metric("📊 Jumlah Kolom", len(df.columns))

    with col3:
        st.metric("❗ Missing Value", int(df.isnull().sum().sum()))

    st.divider()

    # ==========================
    # Search
    # ==========================
    st.subheader("🔍 Pencarian Data")

    keyword = st.text_input("Masukkan kata kunci")

    if keyword:
        hasil = df[df.astype(str).apply(
            lambda x: x.str.contains(keyword, case=False)
        ).any(axis=1)]
        st.dataframe(hasil, use_container_width=True)
    else:
        st.subheader("📋 Dataset")
        st.dataframe(df, use_container_width=True)

    st.divider()

    # ==========================
    # Statistik
    # ==========================
    st.subheader("📈 Statistik Deskriptif")
    st.dataframe(df.describe())

    st.divider()

    # ==========================
    # Grafik
    # ==========================
    numeric_columns = df.select_dtypes(include="number").columns

    if len(numeric_columns) > 0:
        column = st.selectbox(
            "Pilih Kolom Numerik",
            numeric_columns
        )

        st.subheader(f"📊 Grafik {column}")
        st.line_chart(df[column])

    st.divider()

    # ==========================
    # Download
    # ==========================
    st.subheader("📥 Download Dataset")

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download CSV",
        data=
