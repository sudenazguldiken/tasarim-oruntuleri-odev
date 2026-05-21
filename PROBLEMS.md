# Faz 0 - Kod Sorunlari

## Tespit Edilen Problemler

1. Single Responsibility Principle ihlali
   - ShoppingCart sinifi hem sepet yonetimi hem indirim hesaplamasi hem de fis yazdirimasi yapiyor.
   - Bu gorevler ayri siniflara ayrilmali.

2. Open/Closed Principle ihlali
   - Yeni bir indirim turu eklemek icin calculate_total() metodunu acip degistirmek gerekiyor.
   - Her degisiklik mevcut kodu bozma riski tasir.

3. Hardcoded indirim kodlari
   - STUDENT10, SUMMER20, VIP50 kodlari direkt if/elif ile yazilmis.
   - Yeni indirim eklemek icin kaynak kodu degistirmek gerekiyor.

4. Genisletilebilirlik yok
   - Farkli odeme yontemleri, vergi hesaplamasi veya kargo ucreti eklemek cok zor.
   - Her yeni ozellik icin mevcut sinifi degistirmek gerekiyor.

5. Test edilebilirlik dusuk
   - Indirim mantigi ayri bir sinifta olmadigi icin bagimsiz test edilemiyor.

## Yapay Zeka Analizi (Claude)

1. God Class problemi
   - ShoppingCart sinifi cok fazla is yapiyor: urun ekleme, indirim, toplam hesaplama, fis yazdirilmasi.
   - Cozum: Factory Method ile nesne uretimini ayir.

2. Acik/Kapali Prensip ihlali
   - Yeni indirim eklemek icin mevcut kodu degistirmek gerekiyor.
   - Cozum: Strategy Pattern ile her indirim turu ayri sinif olmali.

3. Fis yazdirilmasi yanlis yerde
   - print_receipt() sepet sinifi icinde olmamali, goruntulemek is mantigindan ayri olmali.
   - Cozum: Facade Pattern ile ayri bir ReceiptPrinter sinifi.

4. Genisletilebilirlik yok
   - Vergi, kargo, uyelik puani eklemek icin mevcut kodu degistirmek gerekiyor.
   - Cozum: Decorator Pattern ile yeni ozellikler sarmala.

5. Nesne uretimi kontrolsuz
   - Sepet nesnesi direkt ShoppingCart() ile olusturuluyor.
   - Cozum: Factory Method ile uretimi merkezi bir yere tasI.

6. Observer eksikligi
   - Sepete urun eklenince hicbir bildirim mekanizmasi yok.
   - Cozum: Observer Pattern ile olay dinleme yapisi kur.

## Karsilastirma: Ben vs AI

| Sorun | Ben buldum mu? | AI buldu mu? |
|---|---|---|
| Single Responsibility ihlali | Evet | Evet (God Class olarak) |
| Open/Closed Principle ihlali | Evet | Evet |
| Hardcoded indirim kodlari | Evet | Evet (Strategy ile cozulur dedi) |
| Genisletilebilirlik yok | Evet | Evet |
| Test edilebilirlik dusuk | Evet | Dolayli olarak (ayristirma onerdi) |
| Fis yazdirilmasi yanlis yerde | Hayir | Evet (AI ek olarak buldu) |
| Observer eksikligi | Hayir | Evet (AI ek olarak buldu) |

Sonuc: Temel sorunlari kendim tespit edebildim. AI ek olarak fis yazdirilmasi ve Observer eksikligini de vurguladi.
