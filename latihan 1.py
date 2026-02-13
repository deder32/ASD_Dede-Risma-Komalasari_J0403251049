# ============================================
# Latihan 1 Implementasi fungsi untuk menghapus node dengan nilai tertentu.
# ============================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data): #Fungsi untuk menambahkan data diakhir
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    def display(self):
        temp = self.head
        elements = []
        while temp:
            elements.append(str(temp.data))
            temp = temp.next
        print(" -> ".join(elements) if elements else "List Kosong")

    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

llist = LinkedList()
llist.append(10)
llist.append(20)
llist.append(20)

print("List awal")
llist.display()

llist.delete_node(20)
print("setelah 20 dihapus")
llist.display()
