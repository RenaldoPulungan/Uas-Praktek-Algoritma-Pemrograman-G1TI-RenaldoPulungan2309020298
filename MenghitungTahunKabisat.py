def is_kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False

tahun_input = int(input("Masukkan tahun: "))

if is_kabisat(tahun_input):
    print(f"{tahun_input} adalah tahun kabisat.")
else:
    print(f"{tahun_input} bukan tahun kabisat.")