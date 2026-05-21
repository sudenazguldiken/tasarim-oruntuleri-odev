# Faz 2 - AI Kullanim Logu

## Kullanilan Arac
Claude (claude.ai)

## Sorulan Sorular ve Alinan Cevaplar

### Soru 1
"Decorator pattern'i e-ticaret sepetine nasil uygulayabilirim?"

### Cevap
AI, mevcut ShoppingCart sinifini degistirmeden uzerine sarmalayici siniflar
eklenmesini onerdI. TaxDecorator ve ShippingDecorator siniflari olusturuldu.

### Soru 2
"Facade pattern ne ise yarar, nasil uygulayabilirim?"

### Cevap
AI, karmasik sinif iliskilerini tek bir arayuz arkasinda gizlemek icin
Facade pattern kullanilmasini onerdI. OrderFacade sinifi tum islemleri yonetiyor.

## Kendi Katkim
- Decorator zincirini kurdum (TaxDecorator -> ShippingDecorator)
- OrderFacade sinifini tasarladim
- checkout() metoduna parametreler ekledim

## Ogrendiklerim
Decorator pattern sayesinde mevcut kodu hic degistirmeden yeni ozellikler ekleyebildim.
Facade pattern ise karmasik yapilari basit bir arayuze indirgiyor.
