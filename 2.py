def add_vat(price, vat_percent=18):
    total = price + (price * vat_percent/100)
    return(max(0, round(total, 2)))
price_input = float(input("mehsulun qiymeti: "))
vat_input = input("edv (ötürə bilərsiniz, default 18%): ")
if vat_input.strip() == "":
    print(add_vat(price_input))
else:
    print(add_vat(price_input, float(vat_input)))
