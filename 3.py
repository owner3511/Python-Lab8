def build_username(first, last, year=""):
    username = first.lower() + "." + last.lower()
    if year != "":
        username += str(year)
    return username
ad = input("Adınızı daxil edin: ")
soyad = input("Soyadınızı daxil edin: ")
il = input("Doğum ilinizi daxil edin (istəyə bağlıdır): ")
if il != "":
    netice = build_username(ad, soyad, il)
else:
    netice = build_username(ad, soyad)
print("Yaranan istifadəçi adı:", netice)