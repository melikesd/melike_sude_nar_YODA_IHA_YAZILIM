#Class videolarını izlemeyi tamamlayamadığım için önceki konularla 
#banka hesabı kodumu yyazdım.
bakiye = 1000

print("Banka hesabı menüsü")
print("1- Bakiyeyi gör")
print("2- Para yatır")
print("3- Para çek")
print("4- Çıkış")

choice= input("Yapmak isteidğiniz eylemin satır numarasını girin: ")
#kullanıcıdan hangi işlemi yapmamk istediğini öğrendim buna göre if blokları oluşturacağım

if choice == "1":
        print("Bakiyeniz: ", bakiye)
 elif choice == "2":
        amount = float(input("Yüklemek istediğiniz tutarı giriniz: "))  #inputu küsüratlı sayı da girebilmeleri için float deriz

        if amount >0:
            bakiye += amount          #kullanıcının girdiği tutarı bakiyesine ekleriz
            print("Paranız yüklendi")
            print("Son kalan bakiye: ", bakiye)
        else:
            print("Geçersiz sayı!")

 elif choice == "3":
        amount = float(input("Enter deposit amount: ")) 
        if amount > 0:
            bakiye -= amount
            print("Para çekme işlemi başarılı")
            print("Kalan bakiye", bakiye)
        else:
            print("Geçersiz sayı)

elif choice == "4":
    print("Yine bekleriz")
        break

else:
    print("Geçersiz seçenek lütfen tekrar deneyin!")