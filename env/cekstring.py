import re

# Penyiapan data-data kata penting
daftarkata = []
daftarkata.append("Kuis")
daftarkata.append("Tucil")
daftarkata.append("Tubes")
daftarkata.append("Praktikum")
daftarkata.append("Ujian")

print(daftarkata)

# Penyiapan data-data matkul
daftarmatkul = []
daftarmatkul.append("IF2210")
daftarmatkul.append("OOP")
daftarmatkul.append("IF2211")
daftarmatkul.append("Stima")
daftarmatkul.append("IF2220")
daftarmatkul.append("Probstat")
daftarmatkul.append("IF2230")
daftarmatkul.append("OS")
daftarmatkul.append("IF2240")
daftarmatkul.append("Basdat")
daftarmatkul.append("IF2250")
daftarmatkul.append("RPL")

print(daftarmatkul)

# Program MintaTugas
# Spesifikasi: Meminta tugas
# lalu memvalidasikan input
# berisi tanggal, kode mata
# kuliah, jenis tugas, topik
# tugas.

# Minta input kalimat
temp = input()
kalimat = temp.split()

# Memproses kalimat menggunakan regex dan string matching
# regex_tanggal = ''
# regex_kode = ''
# regex_jenistugas = ''
topik = 'c++|java|brute force|dokumen|implementasi|aplikasi|pl'

if re.search("\d{2}[-/]\d{2}[-/]\d{4}", temp) and re.search("if22[1-5][0-1]", temp) and re.search("Kuis|Tucil|Tubes|Praktikum|Ujian",temp) and re.search(topik,temp):
    print("True")
    # Proses dengan string matching
        
# Untuk menambahkan task baru

# Untuk melihat daftar task yang harus dikerjakan

# Untuk menampilkan deadline dari suatu tak tertentu

# Untuk memperbarui task tertentu

# Untuk menandai suatu task sudah dikerjakan

# Untuk menampilkan opsi help


# Proses input

# Validasi
