import boyermoore as bm
from datetime import date
from util import *
import sqlite3
import re

# Pendefinisian database
db = sqlite3.connect("data.db", check_same_thread=False)

# Keperluan debugging only
db.execute("DROP TABLE IF EXISTS TUGAS")
db.execute("CREATE TABLE TUGAS (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, TIPE VARCHAR(20) NOT NULL, MATKUL VARCHAR(20) NOT NULL, TENGGAT DATETIME NOT NULL, TOPIK VARCHAR(20) NOT NULL)")

temp = ""

# Mendapatkan pesan balasan dari bot
def get_reply(temp): #halo coba cek fitur audio call biar enak koordinasinye
    # Kumpulan regex untuk memeriksa input tambah tugas
    topik = "cpp|java|brute force|dokumen|implementasi|aplikasi|pl|[S|s]tring [M|m]atching|A Star|BFS DFS|Webapp|Engimon|OS"
    tanggal = "\d{2}[-/]\d{2}[-/]\d{4}"
    matkul = "[i|I][F|f]22[1-5][0-1]"
    jenis = "Kuis|Tucil|Tubes|Praktikum|Ujian"
    deadline = "[D|d]eadline"
    x_mgg = "[1-99] [M|m]inggu"
    x_hari = "[1-99] hari|hari ini"
    diganti = "diganti"
    done = "sudah|selesai|kelar"
    bantu = "bantu|lakukan"
    id_task = "[T|t]ask \d "

    # ----------- PEMERIKSAAN KALIMAT USER -----------
    # Mengecek apakah ada keyword tanggal
    adaTanggal = False
    adaInterval = False
    if re.search(tanggal, temp):
        dL_tugas_temp = re.findall(tanggal,temp,flags = 0)
        if (len(dL_tugas_temp) != 1):
            adaInterval = True
            if (dL_tugas_temp[0] > dL_tugas_temp[1]):
                to_date = dL_tugas_temp[0]
                from_date = dL_tugas_temp[1]
            else:
                from_date = dL_tugas_temp[0]
                to_date = dL_tugas_temp[1]
        dL_tugas = dL_tugas_temp[0]
        adaTanggal = True

    # Mengecek apakah ada keyword matkul
    adaMatkul = False
    if re.search(matkul, temp):
        nama_matkul_temp = re.findall(matkul, temp, flags = 0)
        nama_matkul = nama_matkul_temp[0]
        adaMatkul = True

    # Mengecek apakah ada keyword jenis tugas
    adaJenis = False
    if re.search(jenis, temp):
        jenis_tugas_temp = re.findall(jenis, temp, flags = 0)
        jenis_tugas = jenis_tugas_temp[0].replace(" ", "_")
        adaJenis = True

    # Mengecek apakah ada keyword topik
    adaTopik = False
    if re.search(topik, temp):
        topik_tugas_temp = re.findall(topik, temp, flags = 0)
        topik_tugas = topik_tugas_temp[0].replace(" ","_")
        adaTopik = True

    # Mengecek apakah ada kata "deadline"
    adaDeadline = False
    if re.search(deadline, temp):
        adaDeadline = True

    # Mengecek apakah ada kata "X minggu"
    adaMinggu = False
    if re.search(x_mgg, temp):
        num_temp = re.findall(x_mgg, temp, flags = 0)
        num = int(num_temp[0][0])
        adaMinggu = True

    # Mengecek apakah ada kata "X hari" atau "hari ini"
    adaHari = False
    if re.search(x_hari, temp):
        num_temp = re.findall(x_hari, temp, flags = 0)
        if (num_temp[0] == "hari ini"):
            num = 0
        else:
            num = int(num_temp[0][0])
        adaHari = True

    # Mengecek apakah ada kata "diganti"
    adaDiganti = False
    if re.search(diganti, temp):
        adaDiganti = True

    # Mengecek apakah ada kata "sudah/selesai"
    adaSelesai = False
    if re.search(done, temp):
        adaSelesai = True

    # Mengecek apakah ada kata "bantu"
    adaBantu = False
    if re.search(bantu, temp):
        adaBantu = True

    adaId = False
    if re.search(id_task, temp):
        adaId = True
        num_temp = str(re.findall(id_task, temp, flags = 0)).split()
        id_task = int(num_temp[1])

    # ----------- PEMROSESAN KALIMAT USER -----------
    # Menambahkan tugas
    if (adaTanggal and adaMatkul and adaJenis and adaTopik):
        return tambahTaskBaru(dL_tugas, nama_matkul, jenis_tugas, topik_tugas, db)

    # Deadline doang -> tampilin semua
    # Deadline + N minggu
    # Deadline + N hari
    # Deadline + hari ini
    # Deadline + matkul
    elif (adaDeadline and not (adaDiganti)):
        if (adaInterval):
            # Cetak pada interval mingguan
            return lihatSemuaTaskInterval(from_date, to_date, db) # Ini buat ngecek doang

        elif (adaHari):
            # Cetak sampai X hari selanjutnya
            return lihatSemuaTaskHari(num, db)

        elif (adaMinggu):
            # Cetak daftar tugas untuk X minggu selanjutnya
            return lihatSemuaTaskMinggu(num, db)
        
        elif (adaMatkul and not (adaJenis)):
            # Cetak daftar tugas untuk matkul X
            return lihatSemuaTaskMatkul(nama_matkul, db)

        else: 
            # Cetak semua deadline
            return lihatSemuaTask(db)

    # Jenis + N hari/minggu
    elif (adaJenis and adaMinggu):
        # Cetak matkul dengan jenis tugas JENIS selama num weeks ke depan
        return lihatSemuaTaskJenis(num, jenis_tugas, db)

    # Deadline + jenis + kode matkul
    elif (adaDeadline and adaDiganti and adaTanggal and adaId):
        if (updateTask(id_task, dL_tugas, db) == "TASK ADA"):
            return ("Task berhasil diperbaharui!")
        else:
            return ("Task "+str(id_task)+" tidak ada!")

    elif (adaSelesai and adaId):
        if (taskSelesai(id_task, db) == "Task tidak ada."):
            return ("Task " + str(id_task) + " tidak ada!")
        else:
            return ("Task telah ditandai selesai")

    elif (adaBantu):
        return showHelp()

    elif (temp == "exit"):
        return ("Sampai jumpa!")

    else:
        return ("Maaf, pesan tidak dikenali")