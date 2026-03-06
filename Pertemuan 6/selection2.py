# ==============================
# Dede Risma Komalasari
# J0403251049
# Selection sort asceding
# ==============================

def selectionSort(data):
   for fillslot in range(len(data)-1, 0, -1):
        positionOfMin = 0
        for location in range(1, fillslot + 1):
                if data[location] < data[positionOfMin]: # Perbandingan '<' untuk mencari MINIMUM
                    positionOfMin = location
    # Swap
        temp = data[fillslot]
        data[fillslot] = data[positionOfMin]
        data[positionOfMin] = temp
data = [54,26,93,17,77,31,44,55,20]
selectionSort(data)
print(data)