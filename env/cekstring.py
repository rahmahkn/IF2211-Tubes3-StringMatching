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

# if re.search("\d{2}[-/]\d{2}[-/]\d{4}", temp) and re.search("if22[1-5][0-1]", temp) and re.search("Kuis|Tucil|Tubes|Praktikum|Ujian",temp) and re.search(topik,temp):
#     print("True")
    # Proses dengan string matching

# Mengecek apakah ada keyword tanggal
adaTanggal = False
if re.search("\d{2}[-/]\d{2}[-/]\d{4}", temp):
    adaTanggal = True

# if (adaTanggal):
#     print("ada tanggal")

# Mengecek apakah ada keyword matkul
adaMatkul = False
if re.search("if22[1-5][0-1]", temp):
    adaMatkul = True

# if (adaMatkul):
#     print("ada matkul")

# Mengecek apakah ada keyword jenis tugas
adaJenis = False
if re.search("kuis|tucil|tubes|praktikum|ujian", temp):
    adaJenis = True

# if (adaJenis):
#     print("ada jenis")

# Mengecek apakah ada keyword topik
adaTopik = False
if re.search("java", temp):
    adaTopik = True

# Mengecek apakah ada ID
adaID = False
if re.search("id", temp):
    adaID = True

# Mengecek apakah ada kata "deadline"
adaDeadline = False
if re.search("deadline", temp):
    adaDeadline = True

# Mengecek apakah ada kata  "X minggu"
adaMinggu = False
if re.search("[0-9] minggu", temp):
    adaMinggu = True

# Mengecek apakah ada kata "X hari" atau "hari ini"
adaHari = False
if re.search("[0-9] hari|hari ini", temp):
    adaHari = True

# Mengecek apakah ada kata "diganti"
adaDiganti = False
if re.search("diganti", temp):
    adaDiganti = True

# Mengecek apakah ada kata "sudah/selesai"
adaSelesai = False
if re.search("sudah|selesai", temp):
    adaSelesai = True

# Mengecek apakah ada kata "bantu"
adaBantu = False
if re.search("bantu", temp):
    adaBantu = True
        
# Untuk menambahkan task baru (perlu tanggal, matkul, jenis, materi)
def tambahTaskBaru(tgl, matkul, jenis, topik):
    # Nambah ke db
    print(tgl + " " + matkul + " " + jenis + " " + topik) # Ini buat ngecek doang

if (adaTanggal and adaMatkul and adaJenis and adaTopik):
    tambahTaskBaru("testanggal", "stima", "kuis", "string matching") # Ini buat ngecek doang

# Untuk melihat daftar task yang harus dikerjakan
def lihatSemuaTask(from_date, to_date):
    print("Lihat semua task") # Ini buat ngecek doang

if (adaDeadline):
    if (adaMinggu):
        lihatSemuaTask("02/03/2021", "03/04/2021") # Ini buat ngecek doang
        print("Print sampe X minggu selanjutnya") # Ini buat ngecek doang
    elif (adaHari):
        print("Print sampe X hari selanjutnya") # Ini buat ngecek doang
    print("Print semua deadline") # Ini buat ngecek doang

# Deadline doang -> tampilin semua
# Deadline + N minggu
# Deadline + N hari
# Deadline + hari ini

# Untuk menampilkan deadline dari jenis
def showDeadline(jenis, tanggal):
    print("Mau show deadline") # Ini buat ngecek doang

if (adaDeadline):
    print("") # Ini buat ngecek doang

# Jenis + N hari/minggu
# Deadline + jenis + kode matkul

# Untuk memperbarui task tertentu
# Deadline + "diganti" + tanggal
def updateTask(id, tgl):
    # Update yg ada di db
    print("Mengganti deadline " + id + " menjadi tanggal "+ tgl) # Ini buat ngecek doang

if (adaDeadline and adaDiganti and adaTanggal):
    updateTask("stima", "20/02/2021") # Ini buat ngecek doang

# Untuk menandai suatu task sudah dikerjakan
# "Sudah" + "selesai" + ID
def taskSelesai(id):
    print("Task dengan id " + id + " sudah selesai") # Ini buat ngecek doang

if (adaSelesai and adaID):
    taskSelesai("3") # Ini buat ngecek doang

# Untuk menampilkan opsi help
def showHelp():
    print("Ini bakal ngeshow semua opsi help") # Ini buat ngecek doang

if (adaBantu):
    showHelp()