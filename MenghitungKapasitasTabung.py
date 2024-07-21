def hitung_sisa_kapasitas(tabung, air_masuk):
    sisa_kapasitas = tabung - air_masuk
    return max(sisa_kapasitas, 0)

def main():
    kapasitas_tabung = float(input("Masukkan kapasitas tabung: "))
    sisa_kapasitas = kapasitas_tabung

    while sisa_kapasitas > 0:
        try:
            air_masuk = float(input("Masukkan kapasitas air yang masuk: "))
            if air_masuk < 0:
                raise ValueError("Kapasitas air yang masuk tidak boleh negatif.")

            sisa_kapasitas = hitung_sisa_kapasitas(sisa_kapasitas, air_masuk)
            print(f"Sisa kapasitas tabung: {sisa_kapasitas}")

            if sisa_kapasitas == 0:
                print("Tabung penuh. Program berakhir.")
                break
            elif sisa_kapasitas < 0:
                print("Tidak bisa menampung lagi. Program berakhir.")
                break

        except ValueError as e:
            print(f"Error: {e}")
            continue

if __name__ == "__main__":
    main()
