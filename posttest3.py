import os
from datetime import date
from prettytable import PrettyTable

class Node: 
    def __init__(self, nama, id, tanggal, jenis, servis, montir): 
        self.nama = nama
        self.id = id
        self.tanggal = tanggal
        self.jenis = jenis
        self.servis = servis
        self.montir = montir
        self.next = None 
 
class Service: 
    def __init__(self): 
        self.head = None 
     
    def tambah(self, nama, id, tanggal, jenis, servis, montir): 
        new_node = Node(nama, id, tanggal, jenis, servis, montir) 
        if self.head is None: 
            self.head = new_node 
            return 
        current = self.head 
        while current.next: 
            current = current.next 
        current.next = new_node 

    def hapus(self, data):  
        current_node = self.head 
        previous_node = None 
        while current_node: 
            if current_node.id == data: 
                if not previous_node: 
                    self.head = current_node.next 
                else: 
                    previous_node.next = current_node.next 
                del current_node 
                break 
            else: 
                previous_node = current_node 
                current_node = current_node.next

    def tampilan(self): 
        show = PrettyTable(['Nama','ID','Tanggal', 'Jenis', 'Servis', 'Montir'])
        current_node = self.head 
        while current_node: 
            show.add_row([current_node.nama,current_node.id, current_node.tanggal,current_node.jenis,current_node.servis,current_node.montir])
            current_node = current_node.next
        print(show)


a = Service()

while True :
    os.system('cls')
    menu = int(input
("""
|===========================|
|   1. Tambah data service  |
|   2. Lihat data service   |
|   3. Hapus data service   |
|===========================|

Masukkan pilihan anda :  

"""))
    
    if menu == 1:
        ulang = "Y"
        while (ulang == "Y"):
            os.system('cls')
            nama = str(input("Input nama pelanggan (CONTOH : RADJA): "))
            id = str(input("Input ID  pelanggan (CONTOH : LX0000): "))
            tanggal = date.today()
            jenis = str(input("Input jenis kendaraan (CONTOH : SEDAN, SUV, MPV): "))
            servis = str(input("Input jenis service (MESIN, EXTERIOR, INTERIOR): "))
            montir = str(input("Input nama montir (CONTOH : RAJA): "))
            a.tambah(nama, id, tanggal, jenis, servis, montir)
            a.tampilan()
            i = input("Apakah anda ingin menginput data lagi (Y/N) : ")
            if i == "N":
                break
    elif menu == 2:
        ulang = "Y"
        while (ulang == "Y"):
            os.system('cls')
            a.tampilan()
            i = input("Apakah anda ingin menginput data lagi (Y/N) : ")
            if i == "N":
                break
    elif menu ==3:
        ulang = "Y"
        while (ulang == "Y"):
            os.system('cls')
            a.tampilan()
            hapus = str(input("Input ID yang akan dihapus : "))
            a.hapus(hapus)
            a.tampilan()
            i = input("Apakah anda ingin menginput data lagi (Y/N) : ")
            if i == "N":
                break