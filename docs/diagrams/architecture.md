# Mimari Diyagram

## Sinif Yapisi
ShoppingCart
├── add_observer(observer)
├── notify_observers(event, data)
├── add_item(name, price, quantity)
├── apply_discount(code)
├── calculate_total()
└── print_receipt()
DiscountFactory
└── get_discount(code) -> BaseDiscount
├── StudentDiscount (apply: %10)
├── SummerDiscount  (apply: %20)
└── VipDiscount     (apply: %50)
CartDecorator
├── TaxDecorator     (KDV %18 ekler)
└── ShippingDecorator (Kargo 50TL ekler)
OrderFacade
└── checkout(include_tax, include_shipping)
Observer
├── StockObserver        (stok gunceller)
└── NotificationObserver (bildirim gonderir)
## Pattern Iliskileri

- ShoppingCart -> DiscountFactory (Factory Method)
- TaxDecorator -> ShoppingCart    (Decorator)
- ShippingDecorator -> ShoppingCart (Decorator)
- OrderFacade -> ShoppingCart + Decorators (Facade)
- ShoppingCart -> Observer listesi (Observer)
- BaseDiscount -> alt siniflar (Strategy)
