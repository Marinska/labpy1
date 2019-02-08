a = int(input("Masukan nilai pertama : ")) #memperkenalkan variable a dengan nilai int, kemudian menginputkan nilai dari variable a
b = int(input("Masukan nilai kedua : ")) #lakukan hal yang sama pada nilai b dan c
c = int(input("Masukan nilai ketiga : "))

if a > b: #fungsi if, sebuah baris code yang akan menjalankan suatu perintah apabila suatu syarat dari kondisi terpenuhi
	if a > c:
		print("Nilai terbesar dari ketiga bilangan adalah ",a)
	else:
		print("Nilai terbesar dari ketiga bilangan adalah ",c)
elif b > c:
	print("Nilai terbesar dari ketiga bilangan adalah ",b)
