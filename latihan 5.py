
# ================================================
# Latihan 5: Tambahkan	metode	untuk	membalik	(reverse)	sebuah	single	linked	list	
# tanpa	membuat	linked	list	baru
# =================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        
        while current is not None:
            next_node = current.next  # 1. Simpan sisa list
            current.next = prev       # 2. Putar panah
            prev = current            # 3. Geser prev maju
            current = next_node       # 4. Geser current maju
            
        self.head = prev  

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

ll = LinkedList()
elemen = [1, 2, 3, 4, 5]
for e in elemen:
    ll.append(e)

print("Linked List sebelum dibalik:")
ll.display()

ll.reverse()

print("Linked List setelah dibalik:")
ll.display()