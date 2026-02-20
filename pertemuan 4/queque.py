#======================================
#Nama: Dede Risma Komalasari
#Nim: J0403251049
#Kelas: TPL A2
#======================================

#=======================================
#Implementasi dasar: Queque
#=========================================

class Node:
    #konstuktor yang dijalankan secara otomatis ketika class node dipanggil/di instansiasi
    def __init__(self, data):
        self.data = data #Menyimpan data
        self.next = None #pointer ini menunjuk ke note berikutnya (awal = none)

class queque:
    #Buat kostrktor untuk inisisalisai varibale front dan rear
    def __init__(self):
        self.front = None #Node paling depan
        self.rear = None #Node paling belakang

    def is_empty(self):
        return self.front is None
    
    #Membuat fungsi untuk menambahkan data baru
    def enqueque(self,data):
        nodeBaru = Node(data)

        #Jika queque kosong, front dan rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        #jika queque tidak kosong, maka letakkan data baru ke setelah rear, dan jadikan data baru setelah rear
        self.rear.next = nodeBaru #Leakkan data baru pada bagian paling belakang
        self.rear = nodeBaru #JAdikan data baru sebagai rear
    
    def dequeque(self):
        data_terhapus = self.front.data #lihat data paling depan

        self.front =self.front.next

        if self.front is None:
            self.rear = None

    def tampilkan(self):
        current = self.front
        print("Front ->", end=" ")
        while current is not None:
            print(current.data, end="-> ")
            current = current.next
        print (" rear")

#Intantiasi class queque
q = queque()
q.enqueque("A")
q.enqueque("B")
q.enqueque("C")
q.tampilkan()
q.dequeque()
