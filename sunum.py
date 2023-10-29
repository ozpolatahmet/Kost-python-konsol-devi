from collections import Counter

def k_kucuk(k, liste):
    if k > 0 and k <= len(liste):
        liste.sort()  # listeyi küçükten büyüğe sırala
        return liste[k - 1]  # k'ncı küçük elemanı döndür
    else:
        return "Geçersiz k değeri!"

def en_yakin_cift(hedef, liste):
    if len(liste) < 2:
        return "Listede en az iki değer olmalı."

    liste.sort()  # listeyi küçükten büyüğe sırala
    en_yakin = None  # en yakın çifti başlangıçta boş bir değere ayarla
    en_kucuk_fark = float('inf')  # başlangıçta sonsuz bir fark ayarla

    for i in range(len(liste) - 1):
        for j in range(i + 1, len(liste)):
            toplam = liste[i] + liste[j]
            fark = abs(hedef - toplam)
            if fark < en_kucuk_fark:
                en_kucuk_fark = fark
                en_yakin = (liste[i], liste[j])

    return en_yakin

def tekrar_eden_elemanlar(liste):
    tekrar_edenler = [eleman for eleman in liste if liste.count(eleman) > 1]
    return list(set(tekrar_edenler))  # tekrar edenleri bir listeye dönüştür

def matris_carpimi(matris1, matris2):
    # ilk matrisin satır ve sütun sayılarını al
    satir1 = len(matris1)
    sutun1 = len(matris1[0])

    # ikinci matrisin satır ve sütun sayılarını al
    satir2 = len(matris2)
    sutun2 = len(matris2[0])

    # matris çarpımı için uygun boyutta bir sonuç matrisi oluştur
    sonuc = [[0 for _ in range(sutun2)] for _ in range(satir1)]

    # matris çarpımını hesapla
    for i in range(satir1):
        for j in range(sutun2):
            sonuc[i][j] = sum(matris1[i][k] * matris2[k][j] for k in range(satir2))

    return sonuc

def kelime_frekanslari_metin(dosya_konumu):
    try:
        with open(dosya_konumu, 'r', encoding='utf-8') as dosya:
            metin = dosya.read()
            kelimeler = metin.split()
            kelime_sayac = Counter(kelimeler)
            for kelime, frekans in kelime_sayac.items():
                print(f"{kelime} = {frekans}")
    except FileNotFoundError:
        print("Belirtilen dosya bulunamadı.")
    except Exception as e:
        print(f"Bir hata oluştu: {str(e)}")

def en_kucuk_deger(liste):
    if not liste:
        return "Liste Boş."

    en_kucuk = float('inf')  # sonsuz (inf) başlangıçta en küçük olarak kabul edilir.

    for eleman in liste:
        if eleman < en_kucuk:
            en_kucuk = eleman

    return en_kucuk

def karekok(N, x0):
    tol = 1e-10  # varsayılan tolerans
    maxiter = 10  # varsayılan max iterasyon sayısı

    x = x0  # tahmin
    for i in range(maxiter):
        hata = abs(x * x - N)  # hata hesaplama
        if hata < tol:
            return x  # toleransı karşılandığında sonucu döndür
        x = 0.5 * (x + N / x)  # yeni tahmin hesaplama babil yöntemi

    # maksimum iterasyon sayısına ulaştığında uyarı ver
    return f"{maxiter} iterasyonda sonuca ulaşılamadı. 'tol' veya 'maxiter' değerlerini değiştirin."

def eb_ortak_bolen(a, b):
    while b:
        a, b = b, a % b
    return a

def asal_veya_degil(sayi):
    if sayi <= 1:
        return False  # 1 ve negatifler asal değil

    if sayi <= 3:
        return True  # 2 3 asal

    if sayi % 2 == 0 or sayi % 3 == 0:
        return False  #2 3 e bölünenler asal değil

    i = 5
    while i * i <= sayi:
        if sayi % i == 0 or sayi % (i + 2) == 0:
            return False  # 5 veya 7 gibi tüm 6'nın katlarına bölünebilen sayılar asal değil
        i += 6

    return True

def hizlandirici(n, k, fibk, fibk1):
    if n == k:
        return fibk
    else:
        return hizlandirici(n, k + 1, fibk + fibk1, fibk1)

def hizli_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return hizlandirici(n, 2, 1, 0)

while True:
    print("Konsol Menü")
    print("1. k'nıncı En Küçük Elemanı Bul")
    print("2. En Yakın Çifti Bul")
    print("3. Bir Listenin Tekrar Eden Elemanlarını Bul")
    print("4. Matris Çarpımı")
    print("5. Metin Dosyasındaki Kelime Frekanslarını Bul")
    print("6. Liste İçinde En Küçük Değeri Bul")
    print("7. Bir Sayının Karekökünü Bul")
    print("8. İki Sayının En Büyük Ortak Bölgesini Bul")
    print("9. Bir Sayının Asal Olup Olmadığını Kontrol Et")
    print("10. Daha Hızlı Fibonacci Hesabı")
    print("0. Çıkış")

    secim = input("Bir seçenek numarası girin: ")

    if secim == "1":
        k = int(input("k değerini girin: "))
        liste = input("Liste girin (örnek: 7, 10, 4, 3, 20, 15): ").split(",")
        liste = [float(eleman) for eleman in liste]  # girdiyi ondalıklı sayı listesine dönüştür
        sonuc = k_kucuk(k, liste)
        print(f"{k}'ıncı en küçük eleman: {sonuc}")
    elif secim == "2":
        hedef = float(input("İstenilen sayıyı girin: "))
        liste = input("Liste girin (örnek: 10.5, 22.3, 28.7, 30.0): ").split(",")
        sonuc = en_yakin_cift(hedef, liste)
        if sonuc is not None:
            print(f"En yakın çift: {sonuc[0]} ve {sonuc[1]}")
        else:
            print("En yakın çift bulunamadı.")
    elif secim == "3":
        liste = input("Liste girin (örnek: 1.2, 2.8, 2.8, 1.2, 5.0, 6.4, 5.0): ").split(",")
        liste = [float(eleman) for eleman in liste]
        sonuc = tekrar_eden_elemanlar(liste)
        print("Tekrar eden elemanlar:", sonuc)
    elif secim == "4":
        # matris girişlerini al
        matris1 = []
        matris2 = []
        satir1 = int(input("İlk matrisin satır sayısını girin: "))
        sutun1 = int(input("İlk matrisin sütun sayısını girin: "))
        satir2 = int(input("İkinci matrisin satır sayısını girin: "))
        sutun2 = int(input("İkinci matrisin sütun sayısını girin: "))

        print("İlk matrisin elemanlarını girin:")
        for i in range(satir1):
            matris1.append([float(x) for x in input().split()])

        print("İkinci matrisin elemanlarını girin:")
        for i in range(satir2):
            matris2.append([float(x) for x in input().split()])

        # matris çarpımını hesapla
        sonuc = matris_carpimi(matris1, matris2)
        print("Matris Çarpımı Sonucu:")
        for satir in sonuc:
            print(satir)
    elif secim == "5":
        dosya_konumu = input("Metin dosyasının konumunu girin :")
        kelime_frekanslari_metin(dosya_konumu)
    elif secim == "6":
        liste = input("Bir liste girin (örnek: 1,-4,6,91,2,65): ").split(",")
        liste = [float(eleman) for eleman in liste]  
        sonuc = en_kucuk_deger(liste)
        print(f"Listedeki en küçük değer: {sonuc}")
    elif secim == "7":
        sayi = float(input("Karekökü alınacak sayıyı girin: "))
        tahmin = float(input("Tahmin değerini girin: "))
        sonuc = karekok(sayi, tahmin)
        print(f"{sayi}'nin karekökü: {sonuc}")
    elif secim == "8":
        sayi1 = int(input("Birinci sayıyı girin: "))
        sayi2 = int(input("İkinci sayıyı girin: "))
        sonuc = eb_ortak_bolen(sayi1, sayi2)
        print(f"{sayi1} ve {sayi2} sayılarının en büyük ortak böleni: {sonuc}")
    elif secim == "9":
        sayi = int(input("Asallığını kontrol etmek istediğiniz sayoyo girin: "))
        sonuc = asal_veya_degil(sayi)
        print(f"{sayi} sayısı asal mı? {sonuc}")
    elif secim == "10":
        n = int(input("Fibonacci dizisinin kaçıncı elemanını hesaplamak istersiniz? "))
        sonuc = hizli_fibonacci(n)
        print(f"Fibonacci({n}) = {sonuc}")
    elif secim == "0":
        print("Programdan çıkılıyor.")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
