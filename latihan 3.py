# ==========================================
# Latihan 3: Implementasikan	Pencarian	pada	node	tertentu	Double	Linked	List
# ==========================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last
    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" <-> ".join(elements))

    def search(self, key):
        current = self.head
        position = 0

        while current:
            if current.data == key:
                print(f"Elemen {key} ditemukan pada posisi ke {position}")
                return True
            current = current.next
            position += 1

        print(f"Elemen {key} tidak ditemukan dalam list")
        return False
        
dll = DoubleLinkedList()
data_input = [2, 6,	9, 14,	20]

for angka in data_input:
    dll.append(angka)

print("Isi Doubly Linked List: ")
dll.display()

print("Pencarian")
dll.search(9)
