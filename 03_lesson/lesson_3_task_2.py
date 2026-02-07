from smartphone import Smartphone

catalog = catalog = [
    Smartphone("Apple",
               "iPhone 15",
               "+79123456789"),
    Smartphone("Samsung",
               "Galaxy S23",
               "+79234567890"),
    Smartphone("Xiaomi",
               "Redmi Note 12",
               "+79345678901"),
    Smartphone("Google",
               "Pixel 8",
               "+79456789012"),
    Smartphone("OnePlus",
               "11 Pro",
               "+79567890123")
]

for phone in catalog:
    print(f'{phone.phone_brand} - {phone.phone_model}, '
          f'{phone.subscriber_number}')
