import streamlit as st
import random
import time
import pandas as pd
import matplotlib.pyplot as plt

from datetime import timedelta, datetime

def is_viable_Aktivitas_Rekursif(Jadwal, AktL, AktL_End, AktL_Start, index=0):
    if index >= len(Jadwal):
        return True
    AktJ = Jadwal[index]
    AktJ_Start = int(AktJ["Waktu Mulai"].split(":")[0]) * 60 + int(AktJ["Waktu Mulai"].split(":")[1])
    AktJ_End = int(AktJ["Waktu Selesai"].split(":")[0]) * 60 + int(AktJ["Waktu Selesai"].split(":")[1])
    if AktL["Hari"] == AktJ["Hari"]:
        if not (AktL_End <= AktJ_Start or AktL_Start >= AktJ_End):
            return False
    return is_viable_Aktivitas_Rekursif(Jadwal, AktL, AktL_End, AktL_Start, index + 1)

def nonOverlappingSchedule_Rekursif(List, Jadwal, index=0, List_Viable=None):
    if List_Viable is None:
        List_Viable = []
    if index >= len(List):
        return List_Viable
    AktL = List[index]
    AktL_Start = int(AktL["Waktu Mulai"].split(":")[0]) * 60 + int(AktL["Waktu Mulai"].split(":")[1])
    AktL_End = int(AktL["Waktu Selesai"].split(":")[0]) * 60 + int(AktL["Waktu Selesai"].split(":")[1])
    if is_viable_Aktivitas_Rekursif(Jadwal, AktL, AktL_End, AktL_Start):
        List_Viable.append(AktL)
    return nonOverlappingSchedule_Rekursif(List, Jadwal, index + 1, List_Viable)

def is_viable_Aktivitas_Iteratif(Jadwal, AktL, AktL_End, AktL_Start):
    for AktJ in Jadwal:
        AktJ_Start = int(AktJ["Waktu Mulai"].split(":")[0]) * 60 + int(AktJ["Waktu Mulai"].split(":")[1])
        AktJ_End = int(AktJ["Waktu Selesai"].split(":")[0]) * 60 + int(AktJ["Waktu Selesai"].split(":")[1])
        if AktL["Hari"] == AktJ["Hari"]:
            if not (AktL_End <= AktJ_Start or AktL_Start >= AktJ_End):
                return False
    return True

def nonOverlappingSchedule_Iteratif(List, Jadwal):
    List_Viable = []
    for AktL in List:
        AktL_Start = int(AktL["Waktu Mulai"].split(":")[0]) * 60 + int(AktL["Waktu Mulai"].split(":")[1])
        AktL_End = int(AktL["Waktu Selesai"].split(":")[0]) * 60 + int(AktL["Waktu Selesai"].split(":")[1])
        if is_viable_Aktivitas_Iteratif(Jadwal, AktL, AktL_End, AktL_Start):
            List_Viable.append(AktL)
    return List_Viable

# Streamlit UI
st.title("Tugas Besar Analisis Kompleksitas Algoritma")
st.subheader("Perbandingan Iteratif dan Rekursif pada Algoritma nonOverlapping Schedule")
st.text("Oleh:")
st.text("M. Rifqi Dzaky Azhad	103012330009\nFathan Arya Maulana	103012300083")

jadwal_choice = st.sidebar.radio(
    "Input Jadwal",
    ("Default", "Randomized")
)

st.sidebar.header("Settings")
dataset_size = st.sidebar.slider("Dataset Size", 1, 1000, 10)

computer_science_courses = [
    "AGAMA ISLAM", "ALGORITMA DAN PEMROGRAMAN 1", "TEORI BAHASA DAN AUTOMATA", 
    "SISTEM OPERASI", "STRUKTUR DATA", "ANALISIS KOMPLEKSITAS ALGORITMA", 
    "ANALISIS JEJARING SOSIAL", "ANALISIS DAN PERANCANGAN PERANGKAT LUNAK", 
    "ORGANISASI DAN ARSITEKTUR KOMPUTER", "BAHASA INGGRIS", "BAHASA INDONESIA", 
    "INTERAKSI MANUSIA KOMPUTER", "DESAIN INTERAKSI", "FORENSIK DIGITAL", "GENERATIVE AI", 
    "IMPLEMENTASI DAN PENGUJIAN PERANGKAT LUNAK", "MATRIKS DAN RUANG VEKTOR", 
    "IOT DENGAN KEMAMPUAN CERDAS", "KALKULUS", "KEAMANAN SIBER", "KECERDASAN ARTIFISIAL", 
    "KOMPUTASI AWAN DAN TERDISTRIBUSI", "KOMPUTASI PARALEL", "LOGIKA MATEMATIKA", 
    "MANAJEMEN PROJEK TIK", "MATEMATIKA DISKRIT", "SISTEM BASIS DATA", "TEORI PELUANG", 
    "SISTEM KEAMANAN CERDAS", "SISTEM MULTI AGEN", "PANCASILA", "PEMBELAJARAN MESIN", 
    "PEMROGRAMAN BERORIENTASI OBJEK", "PENDIDIKAN KARAKTER", "PENGOLAHAN BAHASA ALAMI", 
    "PENGOLAHAN CITRA DIGITAL", "PENULISAN PROPOSAL", "PROCESS MINING", 
    "REPRESENTASI PENGETAHUAN", "SWARM AND EVOLUTIONARY COMPUTATION", "TATA TULIS ILMIAH", 
    "VERIFIKASI DAN VALIDASI PERANGKAT LUNAK", "VISI KOMPUTER", "VISUALISASI DATA", 
    "WRAP RESEARCHSHIP HUMIC1: APLIKASI BERBASIS WEB UNTUK TELEMEDICINE", 
    "WRAP RESEARCHSHIP HUMIC2: APLIKASI BERBASIS SELULER UNTUK TELEMEDICINE", 
    "WRAP RESEARCHSHIP HUMIC3: KECERDASAN BUATAN TERAPAN DALAM TELEMEDICINE"
]

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

Jadwal = [
    {"Hari": "Wednesday", "Nama Aktivitas": "STRUKTUR DATA", "Waktu Mulai": "15:30", "Waktu Selesai": "18:30"},
    {"Hari": "Saturday", "Nama Aktivitas": "STRUKTUR DATA", "Waktu Mulai": "13:30", "Waktu Selesai": "15:30"},
    {"Hari": "Wednesday", "Nama Aktivitas": "SISTEM BASIS DATA", "Waktu Mulai": "12:30", "Waktu Selesai": "15:30"},
    {"Hari": "Tuesday", "Nama Aktivitas": "ORGANISASI DAN ARSITEKTUR KOMPUTER", "Waktu Mulai": "09:30", "Waktu Selesai": "12:30"},
    {"Hari": "Thursday", "Nama Aktivitas": "ANALISIS KOMPLEKSITAS ALGORITMA", "Waktu Mulai": "09:30", "Waktu Selesai": "11:30"},
    {"Hari": "Friday", "Nama Aktivitas": "TEORI BAHASA DAN AUTOMATA", "Waktu Mulai": "09:30", "Waktu Selesai": "11:30"},
    {"Hari": "Monday", "Nama Aktivitas": "TEORI PELUANG", "Waktu Mulai": "07:30", "Waktu Selesai": "10:30"},
    {"Hari": "Friday", "Nama Aktivitas": "STRUKTUR DATA", "Waktu Mulai": "07:30", "Waktu Selesai": "09:30"}
]

Rekursif_execution_times = []
Iteratif_execution_times = []

for size in range(1, dataset_size + 1):
    List_Kegiatan = []
    for _ in range(size):
        random_day = random.choice(days_of_week)
        random_activity = random.choice(computer_science_courses)
        start_hour = random.randint(8, 17)
        start_minute = 30
        duration = random.randint(1, 5)
        end_hour = start_hour + duration
        end_minute = start_minute
        List_Kegiatan.append({"Hari": random_day, "Nama Aktivitas": random_activity, "Waktu Mulai": f"{start_hour:02}:{start_minute:02}", "Waktu Selesai": f"{end_hour:02}:{end_minute:02}"})

    if jadwal_choice != "Default":
        Jadwal = []
        for _ in range(size):
            random_day = random.choice(days_of_week)
            random_activity = random.choice(computer_science_courses)
            
            start_hour = random.randint(8, 17)
            start_minute = 30
            duration = random.randint(1, 5)
            end_hour = start_hour + duration
            end_minute = start_minute
            
            Jadwal.append({
                "Hari": random_day,
                "Nama Aktivitas": random_activity,
                "Waktu Mulai": f"{start_hour:02}:{start_minute:02}",
                "Waktu Selesai": f"{end_hour:02}:{end_minute:02}",
            })

    start_time = time.time()
    nonOverlappingSchedule_Rekursif(List_Kegiatan, Jadwal)
    Rekursif_execution_times.append(time.time() - start_time)

    start_time = time.time()
    nonOverlappingSchedule_Iteratif(List_Kegiatan, Jadwal)
    Iteratif_execution_times.append(time.time() - start_time)

df = pd.DataFrame({
    'Jumlah Aktivitas': range(1, dataset_size + 1),
    'Waktu Algoritma Rekursif': Rekursif_execution_times,
    'Waktu Algoritma Iteratif': Iteratif_execution_times
})

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df['Jumlah Aktivitas'], df['Waktu Algoritma Rekursif'], 'o', label="Algoritma Rekursif")
ax.plot(df['Jumlah Aktivitas'], df['Waktu Algoritma Iteratif'], 'o', label="Algoritma Iteratif")
ax.set_xlabel('Ukuran List Aktivitas')
ax.set_ylabel('Waktu Eksekusi (Detik)')
ax.set_ylim(0, 0.03)
ax.set_xlim(0)
ax.legend()
ax.grid(True, linestyle="--", linewidth=0.5)
st.pyplot(fig)

st.divider()
st.subheader("Kompleksitas Waktu")

complexities = {
    "nonOverlappingSchedule_Rekursif": "O(nL * nJ)",
    "nonOverlappingSchedule_Iteratif": "O(nL * nJ)"
}

for func, complexity in complexities.items():
    st.write(f"**{func}:** {complexity}")

st.divider()
st.subheader("Algoritma")

st.text("Algoritma Iteratif:")
st.image("snippet_Algoritma_Iteratif.png")

st.text("Algoritma Rekursif:")
st.image("snippet_Algoritma_Rekursif.png")

st.text("Algoritma Loop dengan Jadwal Default:")
st.image("snippet_Comparative_Loop.png")

st.text("Algoritma Loop dengan Jadwal Randomized:")
st.image("snippet_Comparative_Loop_Extended.png")