def tentukan_nilai_akhir(tugas: float, uts: float, uas: float):
    return (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)

def nilai_huruf(nilai_akhir: float):
    if nilai_akhir >= 85:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 55:
        return "C"
    elif nilai_akhir >= 40:
        return "D" 
    elif nilai_akhir >= 0:
        return "E"
    else:
        return "Nilai tidak terdeteksi"
    
def tentukan_kelulusan(huruf: str):
    if huruf in ("A", "B", "C"):
        return "lulus"
    else:
        return "tidak lulus"
    
def main():
    # nilai andi
    nama_1, tugas_1, uts_1, uas_1 = "Andi", 80, 70, 90
    nilai_akhir_1 = tentukan_nilai_akhir(tugas_1, uts_1, uas_1)
    n_huruf_1 = nilai_huruf(nilai_akhir_1)
    ket_1 = tentukan_kelulusan(n_huruf_1)

    # nilai dimas
    nama_2, tugas_2, uts_2, uas_2 = "Dimas", 75, 80, 65
    nilai_akhir_2 = tentukan_nilai_akhir(tugas_2, uts_2, uas_2)
    n_huruf_2 = nilai_huruf(nilai_akhir_2)
    ket_2 = tentukan_kelulusan(n_huruf_2)

    
    print(f"Nama: {nama_1} | Nilai Akhir: {nilai_akhir_1} | Huruf: {n_huruf_1} | Keterangan: {ket_1}")
    print(f"Nama: {nama_2} | Nilai Akhir: {nilai_akhir_2} | Huruf: {n_huruf_2} | Keterangan: {ket_2}")

if __name__ == "__main__":
    main()
