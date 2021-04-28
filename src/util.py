import sqlite3
import re
from datetime import date, timedelta

def getDate(tgl):
    x = tgl.replace("-","/")
    x = x.split("/")
    return date(int(x[2]), int(x[1]), int(x[0]))

def cetakTugas(sql,db):
    query = db.execute(sql).fetchall()
    if (len(query) != 0):
        reply = "[DAFTAR TUGAS]\n"
        for i in range(len(query)):
            reply += str(i+1)+". "
            reply += printRow(str(query[i])) + '\n'
    else:
        reply = "Hore! Tidak ada"

    return (reply)

def printRow(query):
    query = query.replace("(","")
    query = query.replace(",","")
    query = query.replace(")","")
    query = query.replace("'","")
    arr_q = query.split()
    reply = "(ID: " + str(arr_q[0]) + ") "
    reply += arr_q[1].replace("_", " ") + " - " + arr_q[2] + " - " + arr_q[3] + " - " + arr_q[4].replace("_"," ")

    return (reply)

def printRowDate(query):
    query = query.replace("(","")
    query = query.replace(",","")
    query = query.replace(")","")
    query = query.replace("'","")
    arr_q = query.split()
    reply = arr_q[3]

    return (reply)

# Untuk menambahkan task baru (perlu tanggal, matkul, jenis, materi)
def tambahTaskBaru(tgl, matkul, jenis, topik, db):

    # Insert to database
    sql = "INSERT INTO TUGAS (tipe, matkul, tenggat, topik) VALUES ('" + jenis + "', '" + matkul + "', '" + str(getDate(tgl)) + "', '" + topik + "')"
    db.execute(sql)
    db.commit()

    id_now = str(db.execute("SELECT max(id) from TUGAS").fetchone())
    id_now = id_now.replace("(","")
    id_now = id_now.replace(",","")
    id_now = id_now.replace(")","")

    # Tampilkan pesan bahwa task telah tercatat
    reply = "[TASK BERHASIL DICATAT]"
    sql = "SELECT * FROM TUGAS WHERE id = " + id_now
    query = str(db.execute(sql).fetchone())
    return printRow(query)

# Untuk menampilkan semua task
def lihatSemuaTask(db):
    sql = "SELECT * FROM TUGAS"

    # Cetak tugas
    return cetakTugas(sql,db)

# Untuk melihat daftar task yang harus dikerjakan antara tanggal_x < tanggal < tanggal_y
def lihatSemuaTaskInterval(from_date, to_date, db):

    # Dapatkan tanggal
    date1 = getDate(from_date)
    date2 = getDate(to_date)

    # Persiapkan query
    sql = "select * from tugas where '"+str(getDate(from_date))+"' <= TENGGAT and TENGGAT <= '"+str(getDate(to_date))+"' order by id"

    # Cetak tugas
    return cetakTugas(sql,db)

def lihatSemuaTaskHari(num, db):
    date_now = date.today()
    date_later = date_now + timedelta(days=num)
    
    # Persiapkan query
    sql = "select * from tugas where '"+str(date_now)+"' <= TENGGAT and TENGGAT <= '"+str(date_later)+"' order by id"

    # Cetak tugas
    return cetakTugas(sql,db)

def lihatSemuaTaskMinggu(num,db):
    date_now = date.today()
    date_later = date_now + timedelta(weeks=num)

    # Persiapkan query
    sql = "select * from tugas where '"+str(date_now)+"' <= TENGGAT and TENGGAT <= '"+str(date_later)+"' order by id"

    # Cetak tugas
    return cetakTugas(sql, db)

def lihatSemuaTaskMatkul(nama_matkul, db):
    sql = "select * from tugas where MATKUL = '" + nama_matkul + "' order by id"

    reply = ""

    query = db.execute(sql).fetchall()
    if (len(query) != 0):
        for i in range(len(query)):
            reply += printRow(str(query[i])) + '\n'
    else:
        reply += "Hore! Tidak ada"

    return (reply)

# Untuk memperbarui task tertentu
# Deadline + "diganti" + tanggal
def updateTask(id, tgl, db):
    sql = "UPDATE TUGAS SET TENGGAT = '" + str(getDate(tgl))+ "' WHERE id = " + str(id)
    db.execute(sql)

# Untuk menandai suatu task sudah dikerjakan
# "Sudah" + "selesai" + ID
def taskSelesai(id, db):
    sql = "DELETE FROM TUGAS WHERE ID = " + str(id)
    db.execute(sql)
    reply = "Task dengan id " + str(id) + " sudah selesai\n" # Ini buat ngecek doang

    return (reply)

# Untuk menampilkan opsi help
def showHelp():
    reply = ""
    reply += "[Fitur]\n"
    reply += "\t1. Menambahkan task baru\n"
    reply += "\t2. Melihat task yang sudah ada\n"
    reply += "\t3. Melihat task berdasarkan kriteria interval tanggal\n"
    reply += "\t4. Melihat task berdasarkan X minggu ke depan\n"
    reply += "\t5. Melihat task berdasarkan X hari ke depan\n"
    reply += "\t6. Memperbaharui deadline suatu task\n"
    reply += "\t7. Memperbaharui status pengerjaan tugas\n\n"
    reply += "[Daftar kata penting]\n"
    reply += "\t1. Kuis\n"
    reply += "\t2. Ujian\n"
    reply += "\t3. Tucil\n"
    reply += "\t4. Tubes\n"
    reply += "\t5. Praktikum\n"
    reply += "\t6. Seluruh kode matkul IF semester 4"

    return (reply)