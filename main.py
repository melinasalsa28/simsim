import streamlit as st
from streamlit_option_menu import option_menu

# navigasi side bar
with st.sidebar:
    selected = option_menu("Aan Rabbits",
                           ["Profil", "Jenis Kelinci", "Siklus Akuntansi", "Laporan Keuangan"],
                           default_index=0)


# Sidebar submenu profil
with st.sidebar:
    if selected == "Profil":
        with st.expander("Tentang"):
            sub_profil = st.radio("Pilih opsi:", ["Alamat", "Kontak"])

# Konten utama
st.title(f"{selected}")

# input data berdasarkan submenu profil
if selected == "Profil":
    if sub_profil == "Alamat":
        st.subheader("ALAMAT")
        alamat = st.write("Karanglo, Barukan, Kecamatan Tengaran, Kabupaten Semarang, Jawa Tengah 50775")

    elif sub_profil == "Kontak":
        st.subheader("KONTAK")
        kontak = st.write("085700182476 (Pak Aan)")

# Sidebar submenu Kelinci
with st.sidebar:
    if selected == "Jenis Kelinci":
        with st.expander("Kelinci"):
            sub_profil = st.radio("Pilih opsi:", ["Jenis Kelinci", "Harga"])


# input data berdasarkan submenu Kelinci
if selected == "Jenis Kelinci":
    if sub_profil == "Jenis Kelinci":
        st.subheader("JENIS KELINCI")
        jenis_kelinci = st.write("masukan dataaaaaaaa")

    elif sub_profil == "Harga":
        st.subheader("HARGA")
        harga = st.write("dataaaa jugaaaaa")

# Sidebar submenu Siklus
with st.sidebar:
    if selected == "Siklus Akuntansi":
        with st.expander("Siklus") :
            sub_profil = st.radio("Pilih opsi:", ["Neraca Saldo Periode Sebelumnya", "Jurnal Umum", "Buku Besar", "Neraca Saldo", "Jurnal Penyesuaian", "Neraca Lajur", "Jurnal Penutup", "Neraca Saldo Setelah Penutupan", "Jurnal Pembalik"])

# input data berdasarkan submenu Siklus
if selected == "Siklus Akuntansi":
    if sub_profil == "Neraca Saldo Periode Sebelumnya":
        st.subheader("NERACA SALDO PERIODE SEBELUMNYA")
        alamat = st.write("masukan dataaaaaaaa")

    elif sub_profil == "Jurnal Umum":
        st.subheader("JURNAL UMUM")
        kontak = st.write("dataaaa jugaaaaa")

    elif sub_profil == "Buku Besar":
        st.subheader("BUKU BESAR")
        kontak = st.write("dataaaa jugaaaaa")

    elif sub_profil == "Neraca Saldo":
        st.subheader("NERACA SALDO")
        kontak = st.write("dataaaa jugaaaaa")
    
    elif sub_profil == "Jurnal Penyesuaian":
        st.subheader("JURNAL PENYESUAIAN")
        kontak = st.write("dataaaa jugaaaaa")

    elif sub_profil == "Neraca Lajur":
        st.subheader("NERACA LAJUR")
        kontak = st.write("dataaaa jugaaaaa")

    elif sub_profil == "Jurnal Penutup":
        st.subheader("JURNAL PENUTUP")
        kontak = st.write("dataaaa jugaaaaa")

    elif sub_profil == "Neraca Saldo Setelah Penutupan":
        st.subheader("NERACA SALDO SETELAH PENUTUPAN")
        kontak = st.write("dataaaa jugaaaaa")
    
    elif sub_profil == "Jurnal Pembalik":
        st.subheader("JURNAL PEMBALIK")
        kontak = st.write("dataaaa jugaaaaa")

# Sidebar submenu Lapkeu
with st.sidebar:
    if selected == "Laporan Keuangan":
        with st.expander("Lapkeu") :
            sub_profil = st.radio("Pilih opsi:", ["Laporan Laba Rugi", "Laporan Perubahan Modal", "Laporan Posisi Keuangan", "Laporan Arus Kas"])

# input data berdasarkan submenu Siklus
if selected == "Laporan Keuangan":
    if sub_profil == "Laporan Laba Rugi":
        st.subheader("LAPORAN LABA RUGI")
        alamat = st.write("masukan dataaaaaaaa")

    elif sub_profil == "Laporan Perubahan Modal":
        st.subheader("LAPORAN PERUBAHAN MODAL")
        kontak = st.write("dataaaa jugaaaaa")

    elif sub_profil == "Laporan Posisi Keuangan":
        st.subheader("LAPORAN POSISI KEUANGAN")
        kontak = st.write("dataaaa jugaaaaa")

    elif sub_profil == "Laporan Arus Kas":
        st.subheader("LAPORAN ARUS KAS")
        kontak = st.write("dataaaa jugaaaaa")


