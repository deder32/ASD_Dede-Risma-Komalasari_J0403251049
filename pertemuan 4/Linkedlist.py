#======================================
#Nama: Dede Risma Komalasari
#Nim: J0403251049
#Kelas: TPL A2
#======================================

#=======================================
#Implementasi dasar: Note pada linked list
#=========================================


class Node:
    #konstuktor yang dijalankan secara otomatis ketika class node dipanggil/di instansiasi
    def __init__(self, data):
        self.data = data #Menyimpan data
        self.next = None #pointer ini menunjuk ke note berikutnya (awal = none)

#1) Membuat none dengan instantiasi class node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2) Menghubungkan Node: A -> B -> C -> None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

#3) Traversal = Menelusuri node darin head sapai none
current = head
while current is not None:
    print(current.data)#Menampikan data pada Node saat ini
    current = current.next #pindah ke node berikutnya

#=======================================
#Implementasi dasar: Stack
#=========================================
