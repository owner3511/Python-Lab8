def add_vat(price, vat_percent=18):
    return price - (price * vat_percent/100)
price = int(input("mehsulun qiymeti: "))
vat_percent = int(input("edv: "))
print(add_vat(price, vat_percent))