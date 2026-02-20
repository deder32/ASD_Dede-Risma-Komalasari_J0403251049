#======================================
#Nama: Dede Risma Komalasari
#Nim: J0403251049
#Kelas: TPL A2
#======================================

#=======================================
#Implementasi dasar: Stack
#=========================================

class Node:
    #konstuktor yang dijalankan secara otomatis ketika class node dipanggil/di instansiasi
    def __init__(self, data):
        self.data = data #Menyimpan data
        self.next = None #pointer ini menunjuk ke note berikutnya (awal = none)

#Stack ada operasi push (memasukkan head baru) dan pop(menghapus head)
# A -> B -> C -> None

class stack:
    def __init__(self):
        self.top = None #top merujuk ke node paling atas (awalnya kosong)
    
    def is_empty(self):
        return self.top is None #stack kosong jika

    def push(self,data): #memasukkan dara baru apda stack
        #1 Membuat node baru
        nodeBaru = Node(data) #instantiasi/memanggil konstruktor pada class Node

        #2 node baru harus merujuk ke top yang palig lama
        nodeBaru.next = self.top

        #3 geser top pindah ke node baru
        self.top = nodeBaru

    def pop(self): #Mengambil atau menghapus node paling atas
        
        if self.is_empty():
            print("Stack kosong, tidak bisa pop")
            return None

        data_terhapus = self.top.data #soroti bagian top dan simpan di variabel
        #B -> A -> None
        self.top = self.top.next
        return data_terhapus

    def peek(self):
        #melihat data yang paling atas
        if self.is_empty():
            return None
        return self.top.data

        # B-> A -> None
    def tampilkan(self):
        #Top -> A -> B
        current = self.top
        print("top ", end='->')
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")

#Instantiasi class stack
stack()
s =stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print("Peek (Lihat top) : ", s.peek)
s.pop()
s.tampilkan()