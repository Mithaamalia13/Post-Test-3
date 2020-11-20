print("="*50)
print("\tSELAMAT DATANG DI TOKO KUE SULE")
print("="*50)

print("\n")
print("="*50)
print("\t\tKue variant KEJU")
print("="*50)

a = int(input("Masukkan jumlah pembelian variant keju  : "))

keju = 6000
stok_keju = 25
if int(4 <= a <= 15):
    print("You get disc 10%")
    harga_asli = a * keju
    print("harga asli : ", harga_asli)
    total1 = a*keju * (10/100)
    diskon1 = harga_asli - total1
    print("Special Price : ",diskon1)
    print("Yang harus dibayar untuk kue keju : ",diskon1)

elif int(16 <= a <= 25):
    print("You get disc 15%")
    harga_asli = a * keju
    print("harga asli : ", harga_asli)
    total2 = a*keju * (15/100)
    diskon1 = harga_asli - total2
    print("Special Price : ",diskon1)
    print("Yang harus dibayar untuk kue keju : ",diskon1)
        
elif (a > 25):
    print("Sorry, stok just 25")

else :
    print("Sorry, you dont get disc")
    jumlah1 = a*keju
    print("Jumlah variant keju : ",jumlah1)
    print("Yang harus dibayar untuk kue keju : ",jumlah1)

stok_keju_sekarang = stok_keju - a
print("Sisa stok keju sekarang adalah : ",stok_keju_sekarang)

print("\n")
print("="*50)
print("\t\tKue variant COKLAT")
print("="*50)

b = int(input("Masukkan jumlah pembelian variant coklat : "))

coklat = 3500
stok_coklat = 35
if int(5 <= b <= 20):
    print("You get disc 7%")
    harga_asli = b * coklat
    print("harga asli : ", harga_asli)
    total3 = b*coklat * (7/100)
    diskon2 = harga_asli - total3
    print("Special Price :",diskon2)
    print("Yang harus dibayar untuk kue coklat: ",diskon2)

elif int(21 <= b <= 35):
    print("You get disc 12%")
    harga_asli = b * coklat
    print("harga asli : ", harga_asli)
    total4 = b*coklat * (12/100)
    diskon2 = harga_asli - total4
    print("Special Price : ",diskon2)
    print("Yang harus dibayar untuk kue coklat: ",diskon2)

elif (b > 35):
    print("Sorry, stok just 25")

else :
    print("Sorry, you dont get disc")
    jumlah2 = b*coklat
    print("Jumlah variant coklat : ",jumlah2)
    print("Yang harus dibayar untuk kue coklat : ",jumlah2)

stok_coklat_sekarang = stok_coklat - b
print("Sisa stok keju sekarang adalah : ",stok_coklat_sekarang)


print("\n")
print("="*50)
print("\t\tTOTAL PEMBELIAN KUE")
print("="*50)

n = int(input("Masukkan jumlah pembelian kue variant KEJU: "))
x = int(input("Masukkan jumlah pembelian kue variant COKLAT: "))

total = x+n
print("Total seluruhnya adalah : ",total)

print("\n")
print("+"*60)
print("\t\t\tTERIMA KASIH")
print("\t\tDITUNGGU KEMBALI DI TOKO SULE")
print("+"*60)