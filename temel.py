
""""  ex1 print komutu
print("19","09","1993",sep = "/") #sep aradaki boşluklara istediğimizi ekliyor
print("{} + {} = {}".format(2,3,2+3))
"""
""" ex2 yorum satırı
python 101
deneme

"""
""" ex3 değişkenler
a = 3
b = 3.14
c = "Python"
d = [1,2,3,4,5,"Python"]
e = (1,2,3,4,5,"Python")
f = {"Elma":3,"Armut":4,"Kiraz":5}
g = False
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

"""
""" ex4 matematik operatörleri
print(3+4)
print(10-3)
print(10*3)
print(10/4)  #float bölme
print(10//4) #tamsayılı bölme
print(10%4)

a = 5
b = 10
c = a + 2 + b

print(c)

a = "Python"
b = "Programlama"
c = "Dili"

d = a + b + c
print(d)

print(a * 5)

print("*" * 1)
print("*" * 2)
print("*" * 3)
print("*" * 4)
print("*" * 5)
"""

""" ex5 string ve listelerin indexlenmesi
a = "Python"
b = [1,2,3,4,5,6,7]

print(a[0])
print(a[2])
print(len(a))
print(len(b))

print(a[5])
print(a[len(a)-1])
print(b[len(b)-1])

print(a[0:2])
print(a[2:])

print(a[:4])
print(b[2:])

print(b[0:6:2]) # iki atlaya atlaya

print(b[::2])

c = {"Elma":3,"Armut":4,"Kiraz":5}

print(c["Elma"])
print(c["Kiraz"])
"""

""" ex6 input alma
#yas = input("Yasinizi Girin:")
#print("Yasiniz: ",yas)

a = input("a:")
b = input("b:")
c = input("c:")
print("Toplam: ",a+b+c)

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
print("Toplam: ",a+b+c)

"""
""" ex7 if else elif
#yas = int(input("Yasinizi Girin:"))

#if yas < 18:
#    print("Mekana Giremezsiniz!")
#else :
#    print("Hoşgeldiniz!")
islem = input("İşlemi giriniz:")

if islem == 1:
    print("İşlem 1' i seçtiniz.")
elif islem == 2:
    print("İşlem 2' yi seçtiniz.")
elif islem == 3:
    print("İşlem 3' ü seçtiniz.")
else:
    print("Gecersiz işlem.")

"""

""" ex8 mantıksal operatörler
a = 3
b = 4

if a==3 and b==4:
    print("Evet")
else:
    print("Hayır")
#and ikisi de sağlamalı
#or biri sağlasa yeterli
#not true ise false yapar, false ise true yapar
"""
""" ex9 while döngüsü
i = 0
while i < 10:
    print("i:",i)
    #i = i + 1
    i += 1

"""
""" ex10 break continue
i=0
while (i<10):
    if i == 5:
        break
    print("i:",i)
    i += 1
#sonsuz döngü
while (i<10):
    if i==3 or i==5:
        #i +=1
        continue
    print("i:",i)
    i += 1
 
"""
""" ex11 for
a = [1,2,3,4,5,6]
b = "Python"
for karakter in b:
    print(karakter)
for sayi in range(20,30):  # for sayi in range (20,30,2): yazsaydık atlaya atlaya gidecekti
    print(sayi)
"""
""" ex12 fonksiyonlar

def selamla():
    print("Merhaba")
    print("Nasılsın?")

def selamla(isim = "İsimsiz"):
    print("Merhaba",isim)

selamla("Cenk")
selamla("Mustafa")
selamla()


selamla()

def toplama(a,b,c):
    print("Toplam:",a+b+c)

toplama(3,4,5)

def toplama(a,b,c):
    return a+b+c

toplam = toplama(3,4,5)
print(toplam)


""" 
""" ex13 listelerin ve stringlerin bazı metodları
liste = [1,2,3,4,5,6]
a = "araba"

print(a.startswith("a")) # a a ile mi başlıyor
print(a.endswith("a"))   # a a ile mi bitiyor

a = a.replace("a","o")
print(a)

liste.append("Python")
print(liste)

liste.pop(0) # içine sayı yazmazsak sonuncu silinir
print(liste)

"""
""" ex14 dosyalar
file = open("dosya.txt","r")   # w yazma/ a append yani ekleme/ r read okuma
file.write("Naber Python\n")
file.write("Naber Java\n")
file.write("Naber C++\n")


file.seek(10)

veri = file.read(15)
print(veri)
for satir in file:
    print(satir)

file.close()


"""

""" ex15 OOP


class Account:
    def __init__(self,isim,numara,bakiye):
        self.isim = isim
        self.numara = numara
        self.bakiye = bakiye
    def hesapBilgileri(self):
        print("İsim : ",self.isim)
        print("Numara : ",self.numara)
        print("Bakiye : ",self.bakiye)
    def paraCek(self,miktar):
        if (self.bakiye - miktar < 0):
            print("Bakiyeniz yeterli değil...")
        else:
            self.bakiye -= miktar
            print("Yeni Bakiye: ",self.bakiye)
    def paraYatir(self,miktar):
        self.bakiye += miktar
        print("Yeni Bakiye: ",self.bakiye)

account = Account("Mustafa Cenk Aydın",123456,1000)

account.hesapBilgileri()

account.paraCek(200)

account.hesapBilgileri()

account.paraYatir(1090)

account.hesapBilgileri()


"""

