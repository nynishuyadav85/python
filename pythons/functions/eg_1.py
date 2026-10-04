def add_vat (price, vat_rate):
    return price * (1 + vat_rate / 100)

orders = [10, 25, 300]

for price in orders:
    final_amout = add_vat(price, 10)
    print(final_amout)