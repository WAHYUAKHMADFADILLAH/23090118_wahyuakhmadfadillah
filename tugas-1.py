def pangkat(a,b):
    hasil = a ** b
    return hasil

a = int(input("Masukan Angka : "))
b = int(input("Masukan Pangkat : "))

hasil_pangkat = pangkat(a,b)
print(f'Hasil {a} pangkat {b} : {hasil_pangkat}')