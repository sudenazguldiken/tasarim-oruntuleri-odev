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

## AI'nin Eksik veya Yanlis Onerdigi Seyler

AI basta Facade pattern icin cok genel bir yapi onerdi.
Checkout metodunda sadece print_receipt() cagirmasi yeterliydi dedi,
ama vergi ve kargo decorator'larini otomatik uygulamak icin
include_tax ve include_shipping parametrelerini kendim eklemek zorunda kaldim.
AI bu detayi atladi.

Ayrica AI Adapter pattern onerisinde bulundu ancak projemizde
farkli arayuzleri birlestirme ihtiyaci yoktu, bu yuzden Adapter yerine
Facade secmek daha dogru bir karar oldu.
