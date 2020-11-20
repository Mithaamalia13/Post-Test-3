#NIM 2009106028
NIM = int(input("Masukkan NIM anda : "))
i = 1
x = 1
while x <= NIM+10:
  print(i)
  i += 1
  if i == 10:
    i -= 9
  x += 1