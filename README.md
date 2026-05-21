# Yazilim Tasarim Oruntuleri Odevi
## E-Ticaret Sepeti - Python

Bu proje, yazilim tasarim oruntuleri dersinin odevi kapsaminda gelistirilmistir.
E-ticaret sepeti uzerinde 5 farkli tasarim oruntu uygulanmistir.

## Uygulanan Tasarim Oruntuleri

### Faz 1 - Creational
- **Factory Method**: Indirim nesnelerini merkezi bir fabrika sinifi uretiyor

### Faz 2 - Structural
- **Decorator**: Sepete KDV ve kargo ucreti sarmalamayla ekleniyor
- **Facade**: Karmasik sepet islemleri tek bir arayuzden yonetiliyor

### Faz 3 - Behavioral
- **Strategy**: Her indirim algoritmasi ayri bir sinifta, runtime'da degistirilebilir
- **Observer**: Urun ekleme ve indirim olaylari stok ve bildirim sistemlerine iletiliyor

## Proje Yapisi

tasarim-oruntuleri-odev/
- src/
  - cart.py (Ana sepet sinifi)
  - facade.py (Facade pattern)
  - discounts/ (Factory + Strategy)
  - decorators/ (Decorator pattern)
  - observers/ (Observer pattern)
- docs/
  - ai-log/ (AI kullanim loglari)
- PATTERNS.md (Pattern aciklamalari)
- PROBLEMS.md (Faz 0 analizi)

## Kurulum ve Calistirma

python -m venv venv
venv\Scripts\activate
python src/main.py

## Ornek Cikti

[STOK] Laptop urun sepete eklendi, stok guncelleniyor...
[BILDIRIM] Sepetinize Laptop eklendi!
===== FIS =====
Laptop x1 = 15000 TL
TOPLAM: 13950.0 TL
KDV DAHIL TOPLAM: 16461.0 TL
KARGO DAHIL TOPLAM: 16511.0 TL
