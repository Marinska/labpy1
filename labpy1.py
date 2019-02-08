a = int(input("Masukan nilai pertama : "))
b = int(input("Masukan nilai kedua : "))
c = int(input("Masukan nilai ketiga : "))

if a > b:
	if a > c:
		print("Nilai terbesar dari ketiga bilangan adalah ",a)
	else:
		print("Nilai terbesar dari ketiga bilangan adalah ",c)
elif b > c:
	print("Nilai terbesar dari ketiga bilangan adalah ",b)
