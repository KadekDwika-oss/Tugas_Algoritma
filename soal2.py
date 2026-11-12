def tentukan_biaya_berat(berat: int):
    """Menghitung biaya berat paket."""
    if berat <= 2:
        return 10000
    else:
        return 10000 + ((berat - 2) * 4000)

def tentukan_biaya_jarak(jarak: int):
    """Menghitung biaya tambahan jarak."""
    if jarak <= 20:
        return 0
    else:
        return 5000

def hitung_ongkir(berat: int, jarak: int, is_anggota: bool):
    """Menghitung total ongkir setelah diskon 10% jika anggota."""
    jumlahtotal = tentukan_biaya_berat(berat) + tentukan_biaya_jarak(jarak)
    if is_anggota:
        jumlahtotal = int(jumlahtotal * 0.90)  # Diskon 10% untuk anggota
    return jumlahtotal

def main():
    
    nama_1, berat_1, jarak_1, anggota_1 = "Sari", 5, 25, False
    nama_2, berat_2, jarak_2, anggota_2 = "Tono", 5, 25, True
    nama_3, berat_3, jarak_3, anggota_3 = "Umar", 2, 30, True

    
    ongkir_sari = hitung_ongkir(berat_1, jarak_1, anggota_1)
    ongkir_tono = hitung_ongkir(berat_2, jarak_2, anggota_2)
    ongkir_umar = hitung_ongkir(berat_3, jarak_3, anggota_3)

    # Cetak hasil akhir
    print(f"Pelanggan: {nama_1} | Ongkir Akhir: Rp {ongkir_sari:,}")
    print(f"Pelanggan: {nama_2} | Ongkir Akhir: Rp {ongkir_tono:,}")
    print(f"Pelanggan: {nama_3} | Ongkir Akhir: Rp {ongkir_umar:,}")

if __name__ == "__main__":
    main()



    

    