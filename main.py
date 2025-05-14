import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np

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
        jenis_kelinci = st.write("data dimasukann!!!")

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
        st.markdown("Periode 30 April 2025")

        data = {
            "Nama Akun" : [
                "Kas", "Persediaan", "Perlengkapan", "Aset Biologis",
                "Utang Bank", "Modal",
                "JUMLAH"
            ],
            "Debit (Rp)" : [
                21100000.00, 13297000.00, 13155000.00, 184725000.00,
                None, None,
                232277000.00
            ],
            "Kredit (Rp)" : [
                None, None, None, None,
                70000000.00, 162277000.00,
                232277000.00
            ]
        }

        df = pd.DataFrame(data)

        # Format tampilan agar mirip tabel akuntansi
        st.dataframe(df.style.format({
            "Debit (Rp)": "Rp {:,.2f}",
            "Kredit (Rp)": "Rp {:,.2f}"
        }))

    elif sub_profil == "Jurnal Umum":
        st.subheader("JURNAL UMUM")
        st.markdown("Periode 30 April 2025")

    elif sub_profil == "Buku Besar":
        st.subheader("BUKU BESAR")
        st.markdown("**Periode 30 April 2025**")
        

    elif sub_profil == "Neraca Saldo":
        st.subheader("NERACA SALDO")
        st.markdown("**Periode 30 April 2025**")

        data = {
            "Keterangan" : [
                "Kas", "Persediaan", "Perlengkapan", "Aset Biologis",
                "Utang Bank", "Modal", "Penjualan",
                "Beban Pemeliharaan", "Beban Bunga", "Beban Pengiriman", "Beban Listrik", "Beban Air", "Beban Gaji",
                "Jumlah"
            ],
            "Debit (Rp)" : [
                57850000.00, 13897000.00, 13455000.00, 188225000.00,
                None, None, None,
                350000.00, 100000.00, 150000.00, 250000.00, 100000.00, 1000000.00, 275377000.00
            ],
            "Kredit (Rp)" : [
                None, None, None, None,
                69000000.00, 162277000.00, 44100000.00,
                None, None, None, None, None, None, 275377000
            ]
        }

        df = pd.DataFrame(data)

        # Format tampilan agar mirip tabel akuntansi
        st.dataframe(df.style.format({
            "Debit (Rp)": "Rp {:,.2f}",
            "Kredit (Rp)": "Rp {:,.2f}"
        }))

    
    elif sub_profil == "Jurnal Penyesuaian":
        st.subheader("JURNAL PENYESUAIAN")
        kontak = st.write("dataaaa jugaaaaa")

        data = {
            "Keterangan" : [
                "Beban Gaji", "     Utang Gaji"
            ],
            "Debit (Rp)" : [
                193548.00, None
            ],
            "Kredit (Rp)" : [
                None, 193548.00
            ]
        }

        df = pd.DataFrame(data)

        # Format tampilan agar mirip tabel akuntansi
        st.dataframe(df.style.format({
            "Debit (Rp)": "Rp {:,.2f}",
            "Kredit (Rp)": "Rp {:,.2f}"
        }))

    elif sub_profil == "Neraca Lajur":
        st.subheader("NERACA LAJUR")
        kontak = st.write("dataaaa jugaaaaa")

    elif sub_profil == "Jurnal Penutup":
        st.subheader("JURNAL PENUTUP")
        st.markdown("**Periode 30 April 2025**")

        data = {
            "Tanggal": [
                "4/30/2025", "", 
                "4/30/2025", "", "", "", "", "", "",
                "4/30/2025", "",
                ""
            ],
            "Keterangan": [
                "Penjualan", "Ikhtisar laba rugi",
                "Ikhtisar laba rugi", "  Beban Pemeliharaan", "  Beban Bunga", "  Beban Pengiriman", "  Beban Listrik", "  Beban Air", "  Beban Gaji",
                "Ikhtisar laba rugi", "  Modal",
                "TOTAL"
            ],
            "Debit (Rp)": [
                44100000.00, None,
                2143548.00, None, None, None, None, None, None,
                None, None,
                46243548.00
            ],
            "Kredit (Rp)": [
                None, 44100000.00,
                None, 350000.00, 100000.00, 150000.00, 250000.00, 100000.00, 1193548.00,
                None, None,
                46243548.00
            ]
        }

        df = pd.DataFrame(data)

        # Format tampilan agar mirip tabel akuntansi
        st.dataframe(df.style.format({
            "Debit (Rp)": "Rp {:,.2f}",
            "Kredit (Rp)": "Rp {:,.2f}"
        }))

    elif sub_profil == "Neraca Saldo Setelah Penutupan":
        st.subheader("NERACA SALDO SETELAH PENUTUPAN")
        st.markdown("**Periode 30 April 2025**")

        # Data Neraca Saldo Setelah Penutupan
        data = {
            "Keterangan": ["Kas", "Persediaan", "Perlengkapan", "Aset Biologis", "Utang Gaji", "Utang Bank", "Modal"],
            "Debit (Rp)": [57850000, 13897000, 13455000, 188225000, None, None, None],
            "Kredit (Rp)": [None, None, None, None, 193548, 69000000, 204233452]
        }

        # Buat DataFrame
        df = pd.DataFrame(data)

        # Hitung total debit dan kredit
        total_debit = df["Debit (Rp)"].sum()
        total_kredit = df["Kredit (Rp)"].sum()

        # Tambahkan baris total
        total_row = pd.DataFrame({
            "Keterangan": ["JUMLAH"],
            "Debit (Rp)": [total_debit],
            "Kredit (Rp)": [total_kredit]
        })

        df = pd.concat([df, total_row], ignore_index=True)

        # Tampilkan DataFrame di Streamlit
        st.dataframe(df.style.format({"Debit (Rp)": "Rp {:,.2f}", "Kredit (Rp)": "Rp {:,.2f}"}))

    
    elif sub_profil == "Jurnal Pembalik":
        st.subheader("JURNAL PEMBALIK")
        st.markdown("Periode 30 April 2025")

        data = {
            "Keterangan" : [
                "Utang Gaji", "     Beban Gaji"
            ],
            "Debit (Rp)" : [
                193548.00, None
            ],
            "Kredit (Rp)" : [
                None, 193548.00
            ]
        }

        df = pd.DataFrame(data)

        # Format tampilan agar mirip tabel akuntansi
        st.dataframe(df.style.format({
            "Debit (Rp)": "Rp {:,.2f}",
            "Kredit (Rp)": "Rp {:,.2f}"
        }))


# Sidebar submenu Lapkeu
with st.sidebar:
    if selected == "Laporan Keuangan":
        with st.expander("Lapkeu") :
            sub_profil = st.radio("Pilih opsi:", ["Laporan Laba Rugi", "Laporan Perubahan Modal", "Laporan Posisi Keuangan"])

# input data berdasarkan submenu Siklus
if selected == "Laporan Keuangan":
    if sub_profil == "Laporan Laba Rugi":
        st.subheader("LAPORAN LABA RUGI")
        st.markdown("**Periode 30 April 2025**")

        data = {
            "None" : [
                "Pendapatan", "  Penjualan", "Beban", "  Beban Pemeliharaan", "  Beban Bunga", "  Beban Pengiriman",
                "  Beban Listrik", "  Beban Air", "  Beban Gaji", "Total Beban", 
                "TOTAL"
            ],
            "(Rp)" : [
                None, 44100000.00, None, 350000.00, 100000.00, 150000.00,
                250000.00, 100000.00, 1193548.00, 2143548.00,
                41956452.00
            ]
        }

        df = pd.DataFrame(data)

        # Format tampilan agar mirip tabel akuntansi
        st.dataframe(df.style.format({
            "(Rp)": "Rp {:,.2f}"
        }))


    #isi lap perubahan modal
    elif sub_profil == "Laporan Perubahan Modal":
        st.subheader("LAPORAN PERUBAHAN MODAL")
        st.markdown("**Periode yang berakhir 30 April 2025**")

        data_perubahan_modal = [
            ("Modal Awal 31 Maret", 162_277_000),
            ("Laba Bersih", 41_956_452),
            ("Penambahan Modal", 41_956_452),
            ("Modal Akhir 30 April 2025", 204_233_452),
        ]

        for keterangan, jumlah in data_perubahan_modal:
            col1, col2 = st.columns([4, 2])
            with col1:
                if "Akhir" in keterangan:
                    st.markdown(f"**{keterangan}**")
                else:
                    st.write(keterangan)
            with col2:
                if "Akhir" in keterangan:
                    st.markdown(f"**Rp {jumlah:,.2f}**")
                else:
                    st.write(f"Rp {jumlah:,.2f}")

    elif sub_profil == "Laporan Posisi Keuangan":
        st.title("LAPORAN POSISI KEUANGAN")
        st.subheader("Periode 30 April 2025")

        data = {
            "Aset" : [
                "Kas", 
                "Persediaan", 
                "Perlengkapan",
                "Jumlah Aset Lancar",
                "Aset Biologis",
                "Jumlah Aset Tidak Lancar",
                "TOTAL ASET"
            ],
            "Jumlah (Rp)" : [
                57850000.00, 
                13897000.00, 
                13455000.00, 
                85202000.00, 
                188225000.00, 
                188225000.00, 
                273427000.00
            ],
            "Liabilitas & Ekuitas" : [
                "Utang Gaji",
                "Utang Bank",
                "TOTAL LIABILITAS",
                "None",
                "Modal",
                "TOTAL EKUITAS",
                "TOTAL LIABILITAS & EKUITAS"
            ],
            "Jumlah (Rp)" : [
                193548.00, 
                69000000.00, 
                69193548.00, 
                None, 
                204233452.00, 
                204233452.00, 
                273427000.00
            ]
        }

        df = pd.DataFrame(data)

        # Format tampilan agar mirip tabel akuntansi
        st.dataframe(df.style.format({
            "Jumlah (Rp)": "Rp {:,.2f}",
            "Jumlah (Rp)": "Rp {:,.2f}"
        }))





