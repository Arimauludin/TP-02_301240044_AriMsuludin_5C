
import pandas as pd

# Membaca file CSV dari folder yang sama
df = pd.read_csv("Course_Completion_Prediction.csv")

# Menampilkan 5 baris pertama
print("--- 5 BARIS PERTAMA ---")
print(df.head())

# Menampilkan nama semua kolom
print("\n--- NAMA-NAMA KOLOM ---")
print(df.columns.tolist())

# Menampilkan ukuran dataset
print("\n--- UKURAN DATASET ---")
print("Jumlah baris:", df.shape[0])
print("Jumlah kolom:", df.shape[1])

# Memvalidasi variabel penelitian
print("\n--- VALIDASI VARIABEL ---")
print(
    "Time_Spent_Hours tersedia:",
    "Time_Spent_Hours" in df.columns
)
print(
    "Progress_Percentage tersedia:",
    "Progress_Percentage" in df.columns
)

# Analisis hubungan durasi belajar dan kemajuan kursus

print("\n--- ANALISIS DATA ---")

# Menghitung korelasi kedua variabel
korelasi = df["Time_Spent_Hours"].corr(
    df["Progress_Percentage"]
)

print("Nilai korelasi:", round(korelasi, 3))

if korelasi > 0:
    print("Hubungan kedua variabel bersifat positif.")
elif korelasi < 0:
    print("Hubungan kedua variabel bersifat negatif.")
else:
    print("Tidak ada korelasi linear.")
