
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

## Faz 3 - Strategy Pattern

### Neden Bu Pattern?
Indirim hesaplamasi Factory ile ayrilmisti ama her indirim sinifi ayni arayuzu kullaniyordu.
Strategy pattern ile her indirim algoritmasini birbirinden bagimsiz degistirilebilir hale getirdik.

### Nasil Uyguladim?
- base_discount.py: Strategy arayuzu (apply metodu)
- student_discount.py, summer_discount.py, vip_discount.py: Somut stratejiler
- ShoppingCart: Hangi stratejiyi kullanacagini runtime'da belirliyor

## Faz 3 - Observer Pattern

### Neden Bu Pattern?
Sepete urun eklenince veya indirim uygulaninca baska sistemlerin (stok, bildirim) haberdar edilmesi gerekiyordu.
Observer pattern ile ShoppingCart bu sistemleri dogrudan cagirmak zorunda kalmadi.

### Nasil Uyguladim?
- observer.py: Soyut observer sinifi
- stock_observer.py: Stok guncelleme bildirimi
- notification_observer.py: Kullanici bildirimi
- ShoppingCart: Observer listesi tutar, olay olunca hepsini bilgilendirir
