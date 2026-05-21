
## Faz 2 - Decorator Pattern

### Neden Bu Pattern?
Sepete vergi ve kargo ucreti eklemek icin mevcut ShoppingCart sinifini degistirmek yerine
sarmalayici (decorator) siniflar kullandik. Boylece orijinal kodu hic dokunmadan yeni ozellikler ekledik.

### Nasil Uyguladim?
- cart_decorator.py: Temel decorator sinifi
- tax_decorator.py: KDV hesaplamasi ekler (%18)
- shipping_decorator.py: Kargo ucreti ekler (50 TL)

### Faz 2 - Facade Pattern

### Neden Bu Pattern?
Musteri sepet olusturmak, indirim uygulamak, vergi ve kargo eklemek icin
birden fazla sinifla ugrasمak zorunda kalmamali. Facade bu karmasikligi gizler.

### Nasil Uyguladim?
- facade.py: Tek bir arayuz uzerinden tum islemleri yonetir
- checkout() metodu vergi ve kargoyu otomatik uygular
