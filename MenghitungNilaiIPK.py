def hitung_nilai_ipk(sem1, sem2, sem3, sem4 , sem5):
    
    nilai_ipk = 0.2 * sem1 + 0.2 * sem2 + 0.2 * sem3 + 0.2 * sem4 + 0.2 * sem5

    return nilai_ipk

# Input nilai IPK
nama = input("Nama : ")
semester1 = float(input("Nilai IP Semester Ke-1 : "))
semester2 = float(input("Nilai IP Semester Ke-2 : "))
semester3 = float(input("Nilai IP Semester Ke-3 : "))
semester4 = float(input("Nilai IP Semester Ke-4 : "))
semester5 = float(input("Nilai IP Semester Ke-5 : "))

# fungsi untuk menghitung nilai akhir dan menentukan status
hasil = hitung_nilai_ipk(semester1, semester2, semester3, semester4, semester5)

# Menampilkan hasil
print (f"IPK : {hasil}")