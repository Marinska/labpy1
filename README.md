# **Bahasa pemrograman Python
## Program menentukan bilangan terbesar dari tiga buah bilangan yang diinputkan
* Repository ini berisikan materi pembuatan program sederhana, yaitu mengenai cara untuk menentukan nilai terbesar dari tiga buah bilangan yang diinputkan.

## Buat file python
* Tentu langkah awal yang harus kita lakukan adalah membuat file python. Langkah ini dapat dilakukan setelah menyelesaikan semua barisan koding, namun untuk meminimalisir kendala, lebih baik dilakukan diawal
* Caranya, yaitu dengan membuka text editor seperti notepad, notepad++ atau yang lain sebagainya.

![github](https://github.com/Marinska/labpy1/blob/master/1.PNG)

* Kemudian pergi kemenu `File` lalu `Save as`.
* Berikan nama file dengan extention ".py" , yang mengindikasikan sebuah file python.

![github](https://github.com/Marinska/labpy1/blob/master/2.PNG)

## Coding
* Hal selanjutnya yang akan kita lakukan adalah membuat barisan code mengenai alur pengerjaan sebuah program yang kita buat.
* Pada program kali ini, kita akan menggunakan sebuah fungsi kondisi pada bahasa pemrograman yaitu "IF".

## IF
* Fungsi IF dalam bahasa pemograman adalah untuk menjalankan ( mengeksekusi suatu program) yang apabila syaratnya atau syarat tertentu telah terpenuhi yang mana bisa terdiri hanya atas satu keadaan (syarat) atau  banyak keadaan tergantung dari program tersebut.

## Source Code
* Tuliskan source code berikut pada file .py yang sudah dibuat.

```
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
	
```


![github](https://github.com/Marinska/labpy1/blob/master/3.PNG)

* Kemudian save lembar kerja kalian.

## Menjalankan program python
* Untuk menjalankan program python, silahkan buka direktori penyimpanan file python yang telah dibuat, contoh `C:\Users\Marinska\Documents\GitHub\labpy1`.

![github](https://github.com/Marinska/labpy1/blob/master/4.PNG)

* Kemudian, klik kanan pada file python tersebut, lalu pilih edit with IDLE.

![github](https://github.com/Marinska/labpy1/blob/master/5.png)

* Lalu jalankan program dengan me-Run dengan Run Module.

![github](https://github.com/Marinska/labpy1/blob/master/6.png)

## Hasil
* Inputkan 3 buah bilangan, maka program akan menentukan bilangan terbesar dari 3 buah bilangan yang telah diinputkan.

![github](https://github.com/Marinska/labpy1/blob/master/7.PNG)
