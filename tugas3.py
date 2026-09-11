# Tugas Python Basics
# Nama: Dicky Effendy

# 1. Deklarasi Variabel dan Tipe Data
nama = "Dicky Effendy"
umur = 21
tinggi = 165
mahasiswa = True
hobi = ["Gaming", "Coding", "Nonton", "Musik", "Traveling"]

print("=== DATA DIRI ===")
print("Nama:", nama)
print("Umur:", umur)
print("Tinggi:", tinggi)
print("Mahasiswa:", mahasiswa)
print("Hobi:", hobi)

# 2. Manipulasi String
print("\n=== MANIPULASI STRING ===")

kalimat = "Halo, nama saya " + nama
print(kalimat)

print("Panjang nama:", len(nama))
print("Nama huruf besar:", nama.upper())
print("Nama huruf kecil:", nama.lower())

# 3. Operasi Matematika Sederhana
print("\n=== OPERASI MATEMATIKA ===")

angka1 = 20
angka2 = 6

print("Penjumlahan:", angka1 + angka2)
print("Pengurangan:", angka1 - angka2)
print("Perkalian:", angka1 * angka2)
print("Pembagian:", angka1 / angka2)
print("Pembagian bulat:", angka1 // angka2)
print("Sisa pembagian:", angka1 % angka2)

# 4. List dan Akses Elemen
print("\n=== LIST DAN AKSES ELEMEN ===")

print("Daftar hobi:", hobi)
print("Hobi pertama:", hobi[0])
print("Hobi kedua:", hobi[1])

hobi.append("Olahraga")
print("Setelah menambahkan hobi:", hobi)

hobi.remove("Nonton")
print("Setelah menghapus hobi:", hobi)

# 5. Input dari User
print("\n=== INPUT USER ===")

nama_user = input("Masukkan nama Anda: ")
umur_user = input("Masukkan umur Anda: ")

print("Halo, nama saya", nama_user, "dan umur saya", umur_user, "tahun.")