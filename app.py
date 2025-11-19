import streamlit as st

# --- 1. Fungsi Konversi Suhu (diambil dari kode Anda) ---
def konversi_celsius(celsius):
    """Fungsi untuk mengkonversi suhu dari Celsius ke skala lain."""

    # Konversi ke Fahrenheit: F = (C * 9/5) + 32
    fahrenheit = (celsius * 9/5) + 32

    # Konversi ke Reamur: R = C * 4/5
    reamur = celsius * 4/5

    # Konversi ke Kelvin: K = C + 273.15
    kelvin = celsius + 273.15

    # Mengembalikan hasil konversi
    return fahrenheit, reamur, kelvin

# --- 2. Tampilan Streamlit ---
st.title("🌡️ Aplikasi Konversi Suhu Celsius")
st.write("Masukkan nilai suhu dalam Celsius, dan lihat hasilnya dalam Fahrenheit, Reamur, dan Kelvin.")

# Mengambil input nilai Celsius dari pengguna
# Menggunakan st.number_input untuk input angka
nilai_celsius = st.number_input(
    "Masukkan nilai suhu dalam Celsius (°C):",
    value=0.0,
    step=0.1,
    format="%.2f"
)

# Tombol untuk memicu perhitungan dan tampilan
if st.button("Hitung Konversi"):
    
    # Panggil fungsi konversi
    F, R, K = konversi_celsius(nilai_celsius)

    # Tampilkan hasil konversi
    st.subheader("✅ Hasil Konversi Suhu")
    st.info(f"Suhu Awal (Celsius): **{nilai_celsius:.2f} °C**")
    st.markdown("---")
    
    # Gunakan kolom untuk tampilan hasil yang rapi
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Fahrenheit (°F)", value=f"{F:.2f}")
        st.caption(f"Rumus: $F = (C \\times 9/5) + 32$")

    with col2:
        st.metric(label="Reamur (°R)", value=f"{R:.2f}")
        st.caption(f"Rumus: $R = C \\times 4/5$")

    with col3:
        st.metric(label="Kelvin (K)", value=f"{K:.2f}")
        st.caption(f"Rumus: $K = C + 273.15$")
