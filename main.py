# import class dan library
from ast import In
from re import I
from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *

# membuat data
hunians = []
hunians.append(Apartemen("Mark Lee", 3, 3, 70, 1200))
hunians.append(Rumah("Na Jaemin", 5, 2, 50, 450))
hunians.append(Indekos("Zhong Chenle", "Park Jisung", 25, 900))
hunians.append(Rumah("Lee Donghyuck", 1, 4, 60, 900))
hunians.append(Apartemen("Lee Jeno", 1, 2, 30, 900))

# inisialisasi tkinter sebagai root (root window)
root = Tk()
root.title("Praktikum DPBO Python")


# -- tampilan details -- #

def details(index):

    # inisialisasi Toplevel sebagai top (toplevel window)
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    # membuat frame details, diberi nama Data Residen
    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    # menampilkan nama pemilik
    d_nama_pemilik = Label(d_frame, text="Nama Pemilik: " + hunians[index].get_nama_pemilik(), anchor="w").grid(row=0, column=0, sticky="w")

    # jika indekos, menampilkan nama penghuni, selain itu menampilkan jumlah kamar
    if(hunians[index].get_jenis() == "Indekos"):
        d_nama_penghuni = Label(d_frame, text="Nama Penghuni: " + hunians[index].get_nama_penghuni(), anchor="w").grid(row=1, column=0, sticky="w")
    else:
        d_jml_kamar = Label(d_frame, text="Jumlah Kamar: " + str(hunians[index].get_jml_kamar()), anchor="w").grid(row=1, column=0, sticky="w")

    # menampilkan luas tanah
    d_luas_tanah = Label(d_frame, text="Luas Tanah: " + str(hunians[index].get_luas_tanah()), anchor="w").grid(row=2, column=0, sticky="w")

    # menampilkan kapasitas listrik
    d_kapasitas_listrik = Label(d_frame, text="Kapasitas Listrik: " + str(hunians[index].get_kapasitas_listrik()), anchor="w").grid(row=3, column=0, sticky="w")

    # menampilkan dokumen
    d_dokumen = Label(d_frame, text="Dokumen: " + hunians[index].get_dokumen(), anchor="w").grid(row=4, column=0, sticky="w")

    # menampilkan summary
    d_summary = Label(d_frame, text="Summary: " + hunians[index].get_summary(), anchor="w").grid(row=5, column=0, sticky="w")
    
    # membuat container untuk tombol button, diinisialisasi sebagai d_opts
    d_opts = LabelFrame(top, padx=10, pady=10)
    d_opts.pack(padx=10, pady=10)

    # membuat fungsi agar dapat close window details
    def exit():
        top.destroy()

    # membuat tombol exit
    d_exit = Button(d_opts, text="Exit", command=exit)
    d_exit.grid(row=0, column=1)


# -- tampilan data seluruh residen -- #

# membuat frame data seluruh residen
frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
frame.pack(padx=10, pady=10)

# membuat container untuk tombol button, diinisialisasi sebagai opts
opts = LabelFrame(root, padx=10, pady=10)
opts.pack(padx=10, pady=10)

 # membuat tombol add data, dibuat disabled (tidak bisa diklik)
b_add = Button(opts, text="Add Data", state="disabled")
b_add.grid(row=0, column=0)

 # membuat tombol exit
b_exit = Button(opts, text="Exit", command=root.quit)
b_exit.grid(row=0, column=1)

# menampilkan data-data residen
for index, h in enumerate(hunians):
    
    # iterator untuk nomor urut
    idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
    idx.grid(row=index, column=0)

    # menampilkan jenis hunian
    type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
    type.grid(row=index, column=1)

    # jika jenis huniannya indekos tampilkan nama pemilik, selain itu tampilkan nama penghuni
    if h.get_jenis() != "Indekos": 
        name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)
    else:
        name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)

    # buat dan tampilkan tombol details untuk membuka window details
    b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
    b_detail.grid(row=index, column=3)

root.mainloop()
