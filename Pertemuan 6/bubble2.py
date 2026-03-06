# ================================================
# Dede Risma Komalasari
# J0403251049
# Latihan Mengurutkan bilangan secara menaik(ascending) menjadi 
# secara menurun (descending)

def shortBubbleSort(alist):
    exchanges = True
    passum = len(alist)-1
    while passum > 0 and exchanges:
        exchanges = False
        for i in range(passum):
            if alist[i] < alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp   
        passum = passum-1

alist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)