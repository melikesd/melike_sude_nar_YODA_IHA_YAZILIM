metin = input ("Bir cümle veya paragraf yazınız: ")
#kullanıcıdan metni istedik.

#metnin hepsini daha kolay işlem yapabilmek için küçük harfe çevirdim.
metin_kucuk = metin.lower()

#kaç kelime olduğunu bulabilmek için kelimelerini ayırıyoruz.
#split içini boş bırakınca space tuşuşna göre kelimeleri ayırır
kelimeler = metin_kucuk.split()

#toplam kelime sayısı için kelimeler değişkenin boyutunu bulmalıyız.
toplam_kelime = len(kelimeler)

#toplam karakter sayısı  boşlukların da işin içine giridği durumdur bu yüzden length fonksiyonunu direkt metin ile çalıştırırım.
toplam_karakter = len(metin)

#en uzun kelime için kelimeler değişkeninin içindeki her bir kelimenin boyutu en büyük olanı almalıyız
if kelimeler:
    en_uzun_kel = max(len(kelime) for kelime in kelimeler)   #max fonksiyonu değerlerden en büyüğünü seçer
else:
    en_uzun_kel = 0

#her kelimenin kaç kez tekrar ettiğini bulmak için sözlük oluştururuz.
kelime_sayaci = {}  #sözlüğü tanımladım
for kelime in kelimeler:    #listedeki her elemanı tek tek kontrl ediyoruz.
    if kelime in kelime_sayaci:
        kelime_sayaci[kelime] += 1
#eğer kelime sözlükte yoksa ilk ekz geçtiği için 1 ekliyoruz eğer sözlükte varsa +1 ekliyoruz.
    else:
        kelime_sayaci [kelime] =1

#ekrana yazdılarım
print("Toplam kelime sayısı {toplam_kelime}", )
print("Toplam karakter sayısı: {toplam_karakter}")
print("En uzun kelimenin uzunluğu: {en_uzun_kel}")
print("Kelime tekrarları:")
for kelime, sayac in kelime_sayaci.items():
    print(kelime, ":", sayac)
#oluştursuğumuz sözlükte paragraftaki kelimeler ve kelimelerin kaç kere tekrar ettiğinin sayısı dictionary olarak duruyor
#içeriğini .items ile okuyoruz.For döngüsü ile tüm kelimeleri baştan sona .items ile okuyup yazdırıyoruz.
#en kafamı karıştıran ve yapay zekadan yardım aldığım kısım buydu