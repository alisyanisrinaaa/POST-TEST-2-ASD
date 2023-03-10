import os
os.system("cls")

# Nama : Alisya Nisrina Sativa
# NIM  : 2209116005
# Sistem Informasi A 2022

def jumpsearch(var, x):
    b = len(var)

    step = int(b ** 0.5)

    # Mencari block yang mengandung elemen-elemen yang dicari
    left = 0
    right = step
    while right < b and var[right - 1] < x:
        left = right
        right += step
    # Melakukan pencarian linier pada block terakhir jika elemen belum ditemukan
    while left < min(right, b):
        if var[left] == x:
            return left
        elif isinstance(var[left], list):
            for j in range(len(var[left])):
                if var[left][j] == x:
                    return (left, j)
        left += 1

    # Jika elemen tidak ditemukan
    return -1

# List of list yang akan dicari elemennya
var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

# Mencari indeks dari setiap elemen dalam list lst
for i in range(len(var)):
    result = var[i]
    if isinstance(result, list):
        for j in range(len(result)):
            item = result[j]
            index = jumpsearch(var, item)
            if index != -1:
                print(f"{item} di Index {index[0]} Pada Kolom {index[1]}")
    else:
        index = jumpsearch(var, result)
        if index != -1:
            print(f"{result} di Index {index}")