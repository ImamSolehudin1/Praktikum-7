class mahasiswa:
    def __init__(self, nim, nama, tugas, uts, uas):
        self.nim    = nim
        self.nama   = nama
        self.tugas  = tugas
        self.uts    = uts
        self.uas    = uas

    def tambah(self,nim,nama,tugas,uts,uas):
        data.nim.append(nim)
        data.nama.append(nama)
        data.tugas.append(tugas)
        data.uts.append(uts)
        data.uas.append(uas)

    def lihat(self):
        for i in range(len(data.nama)):
            print("|", i+1, "  |", end="")
            print('{0:<25}'.format(self.nama[i]), end="")
            print("|", self.nim[i], end="")
            print("       |", self.tugas[i], end="")
            print("    |", self.uts[i], end="")
            print("  |", self.uas[i], " | ", end="\n")


    def ubah(self,nim,nama,tugas,uts,uas):
        self.nim[none] = nim
        self.nama[none] = nama
        self.tugas[none] = tugas
        self.uts[none] = uts
        self.uas[none] = uas

    def hapus(self):
        del self.nim[none]
        del self.nama[none]
        del self.tugas[none]
        del self.uts[none]
        del self.uas[none]

data = mahasiswa([],[],[],[],[])

while True:
    menu = input("\n[(L)ihat, (T)ambah, (U)bah, (H)apus, (K)eluar]:")
    if menu == "t" or menu == "T":
       print("\n= Menambahkan Data =")
       data.tambah(
           input("Masukkan NIM      : "), 
           input("Masukkan Nama     : "), 
           int(input("Nilai Tugas       : ")), 
           int(input("Nilai UTS         : ")), 
           int(input("Nilai UAS         : "))
           )
       print("\nData berhasil ditambahkan")

    elif menu == "l" or menu == "L":
        print("\n= Melihat Data =\n")
        print("=================================================================")
        print("======================== DAFTAR NILAI MAHASISWA =================")
        print("=================================================================")
        print("| No  |          Nama           |    NIM    | TUGAS | UTS | UAS |")
        print("=================================================================")
        if len(data.nama) != 0:
            data.lihat()
        else:
            print("------------------------ TIDAK ADA DATA -------------------------")
        print("=================================================================")

    elif menu == "u" or menu == "U":
        print("\n= Mengubah Ubah Data =")
        ubah = input("Masukkan Nama : ")
        if ubah in data.nama:
           none = data.nama.index(ubah)
           print("Masukkan Data Baru : ")
           data.ubah(
               input("NIM           : "),
               input("Nama          : "),
               int(input("Nilai Tugas   : ")),
               int(input("Nilai UTS     : ")),
               int(input("Nilai UAS     : "))
               )
        else:
            print(ubah, "Data tidak Terdaftar")

    elif menu == "h" or menu == "H":
        print("\n= Menghapus Data =")
        hapus = input("Masukkan Nama : ")
        if hapus in data.nama:
            none = data.nama.index(hapus)
            data.hapus()
            print("Data", hapus, "Berhasil dihapus")
        else:
            print(hapus, "data tidak terdaftar")

    elif menu == "k" or menu == "K":
        print(" ")
        break

    else:
        print("\nPerintah salah!\n")
