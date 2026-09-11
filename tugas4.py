
# Tugas Python Data Structures
# Nama: Dicky Effendy


# 1. List
print("=== LIST ===")

data = ["Dicky", 21, "Jambi", 170.5, "Python", True]

print("Data awal:", data)
print("Elemen pertama:", data[0])
print("Elemen terakhir:", data[-1])
print("Slicing:", data[1:5:2])

data.append("Mahasiswa")
print("Setelah append:", data)

data.insert(1, "Teknik Informatika")
print("Setelah insert:", data)

data.extend(["Coding", "Gaming"])
print("Setelah extend:", data)

data.pop()
print("Setelah pop:", data)

data.remove(True)
print("Setelah remove:", data)


# 2. Tuple
print("\n=== TUPLE ===")

data_diri = ("Dicky", 21, "Jambi", "Teknik Informatika", 6)

print("Tuple:", data_diri)
print("Jumlah isi tuple:", len(data_diri))
print("Elemen pertama:", data_diri[0])
print("Elemen ketiga:", data_diri[2])

nama, umur, *informasi_lain = data_diri

print("Hasil unpacking:")
print("Nama:", nama)
print("Umur:", umur)
print("Informasi lainnya:", informasi_lain)


# 3. Set
print("\n=== SET ===")

set_a = {"Python", "Java", "C++", "JavaScript", "Python"}
set_b = {"Python", "HTML", "CSS", "JavaScript"}

print("Set A:", set_a)
print("Set B:", set_b)

print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference A - B:", set_a - set_b)
print("Symmetric Difference:", set_a ^ set_b)

print("Jumlah isi Set A:", len(set_a))
print("Duplikat otomatis hilang dari set.")


# 4. Dictionary
print("\n=== DICTIONARY ===")

mahasiswa = {
    "nama": "Dicky Effendy",
    "nim": "8020230158",
    "angkatan": 2023,
    "kota": "Jambi"
}

print("Data mahasiswa:", mahasiswa)

mahasiswa["jurusan"] = "Teknik Informatika"
print("Setelah tambah key:", mahasiswa)

mahasiswa["kota"] = "Jakarta"
print("Setelah mengubah kota:", mahasiswa)

mahasiswa.pop("nim")
print("Setelah menghapus NIM:", mahasiswa)

print("Keys:", mahasiswa.keys())
print("Values:", mahasiswa.values())
print("Items:", mahasiswa.items())

print("Isi dictionary:")
for key, value in mahasiswa.items():
    print(key, ":", value)


# 5. Nested Structures
print("\n=== NESTED STRUCTURES ===")

daftar_buku = [
    {
        "judul": "Belajar Python",
        "penulis": "Andi",
        "tahun": 2023
    },
    {
        "judul": "Dasar Pemrograman",
        "penulis": "Budi",
        "tahun": 2021
    },
    {
        "judul": "Python untuk Pemula",
        "penulis": "Citra",
        "tahun": 2024
    },
    {
        "judul": "Algoritma dan Pemrograman",
        "penulis": "Deni",
        "tahun": 2022
    }
]

print("Daftar judul buku:")

for buku in daftar_buku:
    print("-", buku["judul"])

buku_baru = [buku for buku in daftar_buku if buku["tahun"] >= 2023]

print("\nBuku yang terbit tahun 2023 atau lebih baru:")

for buku in buku_baru:
    print("-", buku["judul"], "(", buku["tahun"], ")")


# 6. Comprehension
print("\n=== COMPREHENSION ===")

angka = list(range(1, 21))

angka_genap = [x for x in angka if x % 2 == 0]
angka_kuadrat = [x ** 2 for x in angka]

print("Angka 1-20:", angka)
print("Angka genap:", angka_genap)
print("Angka kuadrat:", angka_kuadrat)

data_angka = {
    x: "genap" if x % 2 == 0 else "ganjil"
    for x in range(1, 11)
}

print("Keterangan angka 1-10:")
print(data_angka)

kalimat = "Saya sedang belajar Python"

huruf_unik = {
    huruf.lower()
    for huruf in kalimat
    if huruf.isalpha()
}

print("Huruf unik:", huruf_unik)


# 7. Keanggotaan dan pencarian
print("\n=== KEANGGOTAAN DAN PENCARIAN ===")

hobi = ["Gaming", "Coding", "Musik", "Traveling"]

print("Apakah Coding ada di list?", "Coding" in hobi)
print("Apakah Membaca ada di list?", "Membaca" in hobi)

bahasa = {"Python", "Java", "C++"}

print("Apakah Python ada di set?", "Python" in bahasa)
print("Apakah PHP ada di set?", "PHP" in bahasa)

if "Musik" in hobi:
    posisi = hobi.index("Musik")
    print("Musik ditemukan pada posisi:", posisi)
else:
    print("Musik tidak ditemukan.")
