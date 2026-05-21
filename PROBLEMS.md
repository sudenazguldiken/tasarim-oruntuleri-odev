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
