def kodla_mesaj(mesaj, kaydirma):
    # Bu fonksiyon, verilen bir mesajı belirli bir kaydırma sayısı ile kodlar.
    kodlanmis_mesaj = ""  # Kodlanmış mesajı depolamak için boş bir string oluşturuyoruz.
    
    for harf in mesaj:
        if harf.isalpha():  # Sadece harfleri işle, özel karakterleri ve sayıları atla
            buyuk_harf = harf.isupper()  # Harfin büyük harf olup olmadığını kontrol et
            harf = harf.lower()  # Harfi küçük harfe çevir (işlemleri sadece küçük harflerle yapmak için)
            # Harfi kaydırarak kodla ve kodlanmış mesaja ekle
            kodlanmis_harf = chr((ord(harf) - ord('a') + kaydirma) % 26 + ord('a'))
            if buyuk_harf:
                kodlanmis_harf = kodlanmis_harf.upper()  # Eğer orijinal harf büyükse, kodlanmış halini büyük yap
            kodlanmis_mesaj += kodlanmis_harf
        else:
            kodlanmis_mesaj += harf  # Harf harici karakterleri direkt ekleyin (noktalama işaretleri, sayılar, boşluklar, vs.)

    return kodlanmis_mesaj

def coz_mesaj(kodlanmis_mesaj, kaydirma):
    # Bu fonksiyon, kodlanmış bir mesajı belirli bir kaydırma sayısı ile çözer.
    # Kod çözme işlemi, kodlama işleminin tam tersidir.
    return kodla_mesaj(kodlanmis_mesaj, -kaydirma)  # Geriye kaydırarak kodlanmış mesajı çözer.

while True:
    print("Menü:")
    print("Mesajı kodlamak için 1 basınız.")
    print("Mesajın kodunu çözmek için 2 basınız.")
    print("Programdan çıkmak için 3 basınız.")
    
    secim = input("Lütfen bir seçenek girin (1/2/3): ")

    if secim == '1':
        mesaj = input("Lütfen kodlanacak mesajı girin: ")
        try:
            kaydirma = int(input("Lütfen kaydırma sayısı giriniz: "))
            kodlanmis_mesaj = kodla_mesaj(mesaj, kaydirma)
            print("Kodlanmış Mesaj:", kodlanmis_mesaj)
        except ValueError:
            print("Hata: Geçersiz kaydırma sayısı girdiniz. Lütfen bir tam sayı girin.")

    elif secim == '2':
        kodlanmis_mesaj = input("Lütfen çözülecek kodlanmış mesajı giriniz: ")
        try:
            kaydirma = int(input("Lütfen bir kaydırma sayısı giriniz: "))
            orijinal_mesaj = coz_mesaj(kodlanmis_mesaj, kaydirma)
            print("Orijinal Mesaj:", orijinal_mesaj)
        except ValueError:
            print("Hata: Geçersiz kaydırma sayısı girdiniz. Lütfen bir tam sayı girin.")

    elif secim == '3':
        print("Programdan çıkılıyor. İyi günler!")
        break

    else:
        print("Hata: Geçersiz seçenek. Lütfen 1, 2 veya 3 girin.")
