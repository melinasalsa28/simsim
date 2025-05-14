import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import openpyxl

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

        try:
            df = pd.read_excel("excelsim.xlsx", sheet_name="Labrug", header=None)
            df = df.dropna(how="all")  # hapus baris kosong

            for i in range(len(df)):
                keterangan = df.iloc[i, 0]
                jumlah = df.iloc[i, 2]

                # Buat 2 kolom: deskripsi dan nominal
                col1, col2 = st.columns([4, 2])

                with col1:
                    # Teks tebal untuk kategori utama
                    if isinstance(keterangan, str) and (keterangan.strip().lower() in ["pendapatan", "beban"] or "total" in keterangan.lower()):
                        st.markdown(f"**{keterangan}**")
                    else:
                        st.write(keterangan)

                with col2:
                    if pd.notna(jumlah):
                        # Cetak bold untuk baris total
                        if isinstance(keterangan, str) and "total" in keterangan.lower():
                            st.markdown(f"**Rp {jumlah:,.2f}**")
                        else:
                            st.write(f"Rp {jumlah:,.2f}")
                    else:
                        st.write("")

        except Exception as e:
            st.error(f"Gagal memuat laporan laba rugi: {e}")

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

        try:
            df = pd.read_excel("excelsim.xlsx", sheet_name="NRC", header=None)

            # Ambil kolom sesuai struktur: Aset (0,1), Liabilitas+Ekuitas (2,3)
            df_clean = df.dropna(how='all')  # hapus baris kosong

            # Buat 4 kolom
            col1, col2, col3, col4 = st.columns([2, 1.5, 2, 1.5])  # Atur lebar biar rapi

            # Header
            with col1:
                st.markdown("**Aset**")
            with col2:
                st.markdown("**Jumlah (Rp)**")
            with col3:
                st.markdown("**Liabilitas & Ekuitas**")
            with col4:
                st.markdown("**Jumlah (Rp)**")

            # Loop per baris
            for i in range(len(df_clean)):
                a1 = df_clean.iloc[i, 0]
                a2 = df_clean.iloc[i, 1]
                b1 = df_clean.iloc[i, 2]
                b2 = df_clean.iloc[i, 3]

                with col1:
                    if pd.notna(a1):
                        st.write(a1)
                    else:
                        st.write("")

                with col2:
                    if pd.notna(a2):
                        st.write(f"Rp {a2:,.0f}")
                    else:
                        st.write("")

                with col3:
                    if pd.notna(b1):
                        st.write(b1)
                    else:
                        st.write("")

                with col4:
                    if pd.notna(b2):
                        st.write(f"Rp {b2:,.0f}")
                    else:
                        st.write("")

        except Exception as e:
            st.error(f"Gagal menampilkan data: {e}")





