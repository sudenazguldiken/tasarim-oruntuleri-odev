# Faz 3 - AI Kullanim Logu

## Kullanilan Arac
Claude (claude.ai)

## Sorulan Sorular ve Alinan Cevaplar

### Soru 1
"Observer pattern'i e-ticaret sepetine nasil uygulayabilirim?"

### Cevap
AI, ShoppingCart sinifina observer listesi eklenmesini ve urun eklenince
veya indirim uygulaninca tum observer'larin bilgilendirilmesini onerdI.

### Soru 2
"Strategy pattern ile Factory Method arasindaki fark nedir?"

### Cevap
AI, Factory Method'un nesne uretimini yonettigini, Strategy'nin ise
algoritma secimini runtime'da degistirmeye odaklandigini acikladi.

## Kendi Katkim
- StockObserver ve NotificationObserver siniflarini tasarladim
- ShoppingCart'a notify_observers mekanizmasini ekledim
- Tum pattern'leri main.py'de birlesik test ettim

## Ogrendiklerim
Observer pattern sayesinde ShoppingCart baska sistemleri dogrudan cagirmak
zorunda kalmadi. Yeni bir observer eklemek icin mevcut kodu degistirmek gerekmiyor.

## AI Olmadan Ne Kadar Surerdi?

Bu faz AI olmadan en az 3-4 saat surerdi. Observer pattern icin
dogru event mekanizmasini kurmak ve Strategy ile Factory arasindaki
farki anlamak zaman alirdi.

## AI Bizi Nerede Yaniltti?

AI ilk basta Observer icin event sistemi yerine direkt metod cagrisi onerdi.
Yani StockObserver'i ShoppingCart'in icinden dogrudan cagirmami soyledi.
Bu Observer pattern'in amacina aykiri olurdu cunku ShoppingCart observer'lari
tanimamali. Bunu fark edip notify_observers mekanizmasini kendim kurdum.
