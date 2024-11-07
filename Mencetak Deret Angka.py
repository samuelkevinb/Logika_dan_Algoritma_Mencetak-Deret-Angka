def cetak_deret(n, count=1):
    if count > 100:  # Berhenti jika sudah mencetak 100 angka
        return
    print(n, end=" ")
    cetak_deret(n + 2, count + 1)  # Memanggil fungsi secara rekursif untuk angka berikutnya

# Memulai dengan angka 1 dan menghitung dari 1
cetak_deret(1)