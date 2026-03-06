# ======================
# Dede Risma Komalasari
# J0403251049
# ======================

# Program 3 : Implementasi algoritma bubble sort pada python
def bubbleSort(data):
    for passnum in range(len(data)-1,0,-1):
        for i in range(passnum):
            if data[i]>data[i+1]:
                # Tukar dua data bersebelahan yang urutannya salah
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp
data = [54,26,93,17,77,31,44,55,20]
bubbleSort(data)
print(data)

# Program 4: Implementasi algoritma bubble sort yang lebih efisien
def shortBubbleSort(alist):
    exchanges = True
    passum = len(alist)-1
    while passum > 0 and exchanges:
        for i in range(passum):
            if alist[i]>alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp   
        passum = passum-1

alist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)

