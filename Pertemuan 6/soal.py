# =================================
# Dede Risma Komalasari
# J0403251049
# 1. Jika Pak Budi akan meloloskan lima kandidat dengan nilai tertinggi, tuliskanlah
# skor lima kandidat tersebut dari yang paling tinggi hingga terendah.
# 2. Kandidat berapa saja yang lolos?

def selectionSort(data):
    for fillslot in range(len(data)-1, 0, -1):
        positionOfMin = 0
        for location in range(1, fillslot + 1):
            if data[location] < data[positionOfMin]:
                positionOfMin = location

        temp = data[fillslot]
        data[fillslot] = data[positionOfMin]
        data[positionOfMin] = temp

# Data hasil tes potensi akademik
skor = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]

selectionSort(skor)

print("Skor terurut (Descending):", skor)
print("Lima kandidat dengan nilai tertinggi:", skor[:5])