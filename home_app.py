import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np

def show_home():
    # Sidebar
    with st.sidebar:
        selected = option_menu("Farm Flow",
                               ["Profil", "Jenis Kelinci", "Siklus Akuntansi", "Laporan Keuangan"],
                                default_index=0
        )

    with st.sidebar :
        if selected == "Profil":
            with st.expander("Tentang"):
                sub_menu_profil = st.radio("Pilih opsi:", ["Alamat", "Kontak"])


    # Konten utama
    st.title(selected)
    # --- Di bawah ini letakkan konten berdasarkan `selected` dan `sub_menu` seperti sebelumnya ---
    if selected == "Profil":
        if sub_menu_profil == "Alamat":
            st.subheader("ALAMAT")
            st.write("Karanglo, Barukan, Kecamatan Tengaran, Kabupaten Semarang, Jawa Tengah 50775")
        elif sub_menu_profil == "Kontak":
            st.subheader("KONTAK")
            st.write("085700182476 (Pak Aan)")
   # Sidebar submenu Kelinci
    with st.sidebar:
        if selected == "Jenis Kelinci":
            with st.expander("Kelinci"):
                sub_menu_jenis_kelinci = st.radio("Pilih opsi:", ["Jenis Kelinci", "Harga"])


# input data berdasarkan submenu Kelinci
        if selected == "Jenis Kelinci":
            if sub_menu_jenis_kelinci == "Jenis Kelinci":
                st.subheader("JENIS KELINCI")
                jenis_kelinci = st.write("data dimasukann!!!")

            elif sub_menu_jenis_kelinci == "Harga":
                st.subheader("HARGA")
                harga = st.write("dataaaa jugaaaaa")

# Sidebar submenu Siklus
    with st.sidebar:
        if selected == "Siklus Akuntansi":
            with st.expander("Siklus") :
                sub_menu_siklus = st.radio("Pilih opsi:", ["Neraca Saldo Periode Sebelumnya", "Jurnal Umum", "Buku Besar", "Neraca Saldo", "Jurnal Penyesuaian", "Neraca Lajur", "Jurnal Penutup", "Neraca Saldo Setelah Penutupan", "Jurnal Pembalik"])

# input data berdasarkan submenu Siklus
    if selected == "Siklus Akuntansi":
        if sub_menu_siklus == "Neraca Saldo Periode Sebelumnya":
            st.subheader("NERACA SALDO PERIODE SEBELUMNYA")
            st.markdown("Periode 30 April 2025")

            data = {
                    "Nama Akun" : [
                    "Kas", "Persediaan", "Perlengkapan", "Persediaan Kelinci",
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

        elif sub_menu_siklus == "Jurnal Umum":
            st.subheader("JURNAL UMUM")
            st.markdown("Periode 30 April 2025")
            data = {
                "Tanggal" : [
                    "4/04/2025", None,
                    "4/05/2025", None,
                    "4/06/2025", None,
                    "4/07/2025", None,
                    "4/08/2025", None,
                    "4/09/2025", None, None,
                    "4/10/2025", None,
                    "4/12/2025", None,
                    "4/13/2025", None,
                    "4/15/2025", None,
                    "4/16/2025", None,
                    "4/18/2025", None,
                    "4/19/2025", None,
                    "4/20/2025", None,
                    "4/25/2025", None,
                    None
                ],
                "Keterangan" : [
                    "Persediaan Kelinci", "    Kas",
                    "Kas", "    Penjualan",
                    "Beban Pemeliharaan", "    Kas",
                    "Kas", "    Penjualan",
                    "Kas", "    Penjualan",
                    "Utang Bank", "Beban Bunga", "    Kas",
                    "Perlengkapan", "    Kas",
                    "Kas", "    Penjualan",
                    "Beban Pengiriman", "    Kas",
                    "Beban Listrik", "    Kas",
                    "Beban Air", "    Kas",
                    "Persediaan Kelinci", "    Kas",
                    "Kas", "    Penjualan",
                    "Persediaan", "    Kas",
                    "Beban Gaji", "    Kas",
                    "JUMLAH"
                ],
                "Debit (Rp)" : [
                    2000000.00, None,
                    9000000.00, None,
                    350000.00, None,
                    7500000.00, None,
                    5600000.00, None,
                    1000000.00, 100000, None,
                    300000.00, None,
                    12000000.00, None,
                    150000.00, None,
                    250000.00, None,
                    100000.00, None,
                    1500000.00, None,
                    10000000.00, None,
                    600000.00, None,
                    1000000.00, None,
                    51450000.00
                ],
                "Kredit (Rp)" : [
                    None, 2000000.00,
                    None, 9000000.00,
                    None, 350000.00,
                    None, 7500000.00,
                    None, 5600000.00,
                    None, None, 1100000.00,
                    None, 300000.00,
                    None, 12000000.00,
                    None, 150000.00,
                    None, 250000.00,
                    None, 100000.00,
                    None, 1500000.00,
                    None, 10000000.00,
                    None, 600000.00,
                    None, 1000000.00,
                    51450000.00
                ]
            }

            df = pd.DataFrame(data)

            # Format tampilan agar mirip tabel akuntansi
            st.dataframe(df.style.format({
                    "Debit (Rp)": "Rp {:,.2f}",
                    "Kredit (Rp)": "Rp {:,.2f}"
                }))


        elif sub_menu_siklus == "Buku Besar":
            st.subheader("BUKU BESAR")
            st.markdown("**Periode 30 April 2025**")
        

        elif sub_menu_siklus == "Neraca Saldo":
            st.subheader("NERACA SALDO")
            st.markdown("**Periode 30 April 2025**")

            data = {
                "Keterangan" : [
                    "Kas", "Persediaan", "Perlengkapan", "Persediaan Kelinci",
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

    
        elif sub_menu_siklus == "Jurnal Penyesuaian":
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

        elif sub_menu_siklus == "Neraca Lajur":
            st.subheader("NERACA LAJUR")
            kontak = st.write("dataaaa jugaaaaa")

        elif sub_menu_siklus == "Jurnal Penutup":
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

        elif sub_menu_siklus == "Neraca Saldo Setelah Penutupan":
            st.subheader("NERACA SALDO SETELAH PENUTUPAN")
            st.markdown("**Periode 30 April 2025**")

        # Data Neraca Saldo Setelah Penutupan
            data = {
                "Keterangan": ["Kas", "Persediaan", "Perlengkapan", "Persediaan Kelinci", "Utang Gaji", "Utang Bank", "Modal"],
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

    
        elif sub_menu_siklus == "Jurnal Pembalik":
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
                sub_menu_lapkeu = st.radio("Pilih opsi:", ["Laporan Laba Rugi", "Laporan Perubahan Modal", "Laporan Posisi Keuangan"])

# input data berdasarkan submenu Siklus
    if selected == "Laporan Keuangan":
        if sub_menu_lapkeu == "Laporan Laba Rugi":
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
                    "Debit (Rp)": "Rp {:,.2f}",
                    "Kredit (Rp)": "Rp {:,.2f}"
                }))


    #isi lap perubahan modal
        elif sub_menu_lapkeu == "Laporan Perubahan Modal":
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

        elif sub_menu_lapkeu == "Laporan Posisi Keuangan":
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
                    "Jumlah Aset (Rp)" : [
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
                        "-",
                        "Modal",
                        "TOTAL EKUITAS",
                        "TOTAL LIABILITAS & EKUITAS"
                    ],
                    "Jumlah Liabilitas & Ekuitas (Rp)" : [
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
                    "Debit (Rp)": "Rp {:,.2f}",
                    "Kredit (Rp)": "Rp {:,.2f}"
                }))

        if st.button("Logout"):
            st.session_state.logged_in = False
            st.experimental_rerun()






