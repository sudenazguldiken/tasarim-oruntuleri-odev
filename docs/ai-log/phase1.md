# Faz 1 - AI Kullanim Logu

## Kullanilan Arac
Claude (claude.ai)

## Sorulan Sorular ve Alinan Cevaplar

### Soru 1
"Factory Method pattern'i e-ticaret sepetine nasil uygulayabilirim?"

### Cevap
AI, soyut bir temel indirim sinifi (BaseDiscount) olusturulmasini,
her indirim turunun bu siniftan turetilmesini ve bir fabrika sinifinin
dogru indirim nesnesini uretmesini onerdI.

## Kendi Katkim
- Sinif yapisini kendim kurdum
- apply() metod adini duzelttim
- base_discount.py deki abstract metod sorununu cozdum

## Ogrendiklerim
Factory Method pattern sayesinde yeni indirim eklemek artik cok kolay.
Sadece yeni bir sinif olusturup DiscountFactory'e eklemek yeterli.
Mevcut kodu degistirmek gerekmiyor.
