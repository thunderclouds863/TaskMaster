from datetime import datetime

# Fungsi untuk menampilkan menu utama
def tampilkan_menu():
    print("\n--- TaskMaster Menu ---")
    print("1. Tambah Tugas")
    print("2. Tampilkan Daftar Tugas")
    print("3. Edit Tugas")
    print("4. Hapus Tugas")
    print("5. Cari Tugas")
    print("6. Urutkan Tugas")
    print("7. Tampilkan Statistik Tugas")
    print("8. Keluar")

# Fungsi untuk memvalidasi tanggal
def validasi_tanggal(tanggal):
    try:
        datetime.strptime(tanggal, "%d/%m/%Y")
        return True
    except ValueError:
        return False

# Fungsi untuk menambah tugas
def tambah_tugas(tugas_list):
    nama_tugas_input = input("Masukkan nama tugas (bisa lebih dari satu, pisahkan dengan koma): ")
    daftar_nama_tugas = nama_tugas_input.split(",")  # Membagi input nama tugas ke dalam array

    for nama in daftar_nama_tugas:
        nama = nama.strip()  # Menghilangkan spasi ekstra
        deskripsi = input(f"Masukkan deskripsi tugas untuk {nama}: ")

        # Validasi tanggal
        while True:
            tenggat_waktu = input(f"Masukkan tenggat waktu untuk {nama} (format dd/mm/yyyy): ")
            if validasi_tanggal(tenggat_waktu):
                break
            else:
                print("Tanggal tidak valid. Pastikan format dd/mm/yyyy dan tanggal benar.")

        status = input(f"Masukkan status tugas untuk {nama} (Belum Dikerjakan/Sedang Dikerjakan/Selesai Dikerjakan): ")

        # Validasi prioritas
        while True:
            prioritas = input(f"Masukkan prioritas tugas untuk {nama} (Rendah/Sedang/Tinggi): ")
            if prioritas in ["Rendah", "rendah", "Sedang", "sedang", "Tinggi", "tinggi"]:
                break
            else:
                print("Prioritas tidak valid. Pilih antara Rendah, Sedang, atau Tinggi.")

        tugas = [nama, deskripsi, tenggat_waktu, status, prioritas]  # Menggunakan list
        tugas_list.append(tugas)
        print(f"Tugas '{nama}' berhasil ditambahkan!")

# Fungsi untuk menampilkan semua tugas
def tampilkan_daftar_tugas(tugas_list):
    if not tugas_list:
        print("\nDaftar tugas kosong.")
    else:
        print("\n--- Daftar Tugas ---")
        for idx, tugas in enumerate(tugas_list, start=1):
            print(f"{idx}. Nama: {tugas[0]}, Deskripsi: {tugas[1]}, Tenggat Waktu: {tugas[2]}, Status: {tugas[3]}, Prioritas: {tugas[4]}")

# Fungsi untuk menghitung statistik tugas
def tampilkan_statistik_tugas(tugas_list):
    statistik = [0, 0, 0]  # [Belum Dikerjakan, Sedang Dikerjakan, Selesai Dikerjakan]

    for tugas in tugas_list:
        if tugas[3] == "Belum Dikerjakan":
            statistik[0] += 1
        elif tugas[3] == "Sedang Dikerjakan":
            statistik[1] += 1
        elif tugas[3] == "Selesai Dikerjakan":
            statistik[2] += 1

    print("\n--- Statistik Tugas ---")
    print(f"Belum Dikerjakan: {statistik[0]} tugas")
    print(f"Sedang Dikerjakan: {statistik[1]} tugas")
    print(f"Selesai Dikerjakan: {statistik[2]} tugas")

# Fungsi untuk mengedit tugas
def edit_tugas(tugas_list):
    tampilkan_daftar_tugas(tugas_list)
    if tugas_list:
        try:
            index = int(input("\nMasukkan nomor tugas yang ingin diedit: ")) - 1
            if 0 <= index < len(tugas_list):
                tugas = tugas_list[index]  # Ambil tugas sebagai list
                print(f"\nMengedit tugas: {tugas[0]}")

                nama_baru = input("Masukkan nama tugas baru (biarkan kosong jika tidak ingin mengubah): ")
                deskripsi_baru = input("Masukkan deskripsi tugas baru (biarkan kosong jika tidak ingin mengubah): ")

                tenggat_waktu_baru = input("Masukkan tenggat waktu baru (format dd/mm/yyyy atau biarkan kosong): ")
                if tenggat_waktu_baru and not validasi_tanggal(tenggat_waktu_baru):
                    print("Tanggal tidak valid. Tenggat waktu tidak diubah.")
                    tenggat_waktu_baru = None

                status_baru = input("Masukkan status baru (Belum Dikerjakan/Sedang Dikerjakan/Selesai Dikerjakan): ")
                prioritas_baru = input("Masukkan prioritas baru (Rendah/Sedang/Tinggi atau biarkan kosong): ")

                if nama_baru:
                    tugas[0] = nama_baru
                if deskripsi_baru:
                    tugas[1] = deskripsi_baru
                if tenggat_waktu_baru:
                    tugas[2] = tenggat_waktu_baru
                if status_baru:
                    tugas[3] = status_baru
                if prioritas_baru in ["Rendah", "Sedang", "Tinggi"]:
                    tugas[4] = prioritas_baru

                print("Tugas berhasil diperbarui!")
            else:
                print("Nomor tugas tidak valid.")
        except ValueError:
            print("Input tidak valid.")

# Fungsi untuk menghapus tugas
def hapus_tugas(tugas_list):
    tampilkan_daftar_tugas(tugas_list)
    if tugas_list:
        try:
            index_input = input("\nMasukkan nomor tugas yang ingin dihapus (atau ketik 'cancel' untuk kembali): ")
            if index_input.lower() == 'cancel':
                print("Kembali ke menu utama.")
                return  # Kembali ke menu utama

            index = int(index_input) - 1
            if 0 <= index < len(tugas_list):
                konfirmasi = input("Apakah Anda yakin ingin menghapus tugas ini? (y/n): ")
                if konfirmasi.lower() == 'y':
                    tugas_terhapus = tugas_list.pop(index)
                    print(f"Tugas '{tugas_terhapus[0]}' berhasil dihapus!")
                else:
                    print("Penghapusan tugas dibatalkan.")
            else:
                print("Nomor tugas tidak valid.")
        except ValueError:
            print("Input tidak valid.")


# Fungsi untuk mencari tugas
def cari_tugas(tugas_list):
    kriteria = input("Cari berdasarkan nama, status, atau deskripsi? (nama/status/deskripsi): ")

    if kriteria == "nama":
        keyword = input("Masukkan nama tugas yang ingin dicari: ")
        hasil_pencarian = [tugas for tugas in tugas_list if keyword.lower() in tugas[0].lower()]
    elif kriteria == "status":
        keyword = input("Masukkan status yang ingin dicari (Belum Dikerjakan/Sedang Dikerjakan/Selesai Dikerjakan): ")
        hasil_pencarian = [tugas for tugas in tugas_list if tugas[3].lower() == keyword.lower()]
    elif kriteria == "deskripsi":
        keyword = input("Masukkan deskripsi tugas yang ingin dicari: ")
        hasil_pencarian = [tugas for tugas in tugas_list if keyword.lower() in tugas[1].lower()]
    else:
        print("Kriteria tidak valid.")
        return

    if hasil_pencarian:
        print("\n--- Hasil Pencarian ---")
        for tugas in hasil_pencarian:
            print(f"Nama: {tugas[0]}, Deskripsi: {tugas[1]}, Tenggat Waktu: {tugas[2]}, Status: {tugas[3]}, Prioritas: {tugas[4]}")
    else:
        print("Tugas tidak ditemukan.")

# Fungsi untuk mengurutkan tugas
def urutkan_tugas(tugas_list):
    kriteria = input("Urutkan berdasarkan (tenggat/prioritas): ")

    if kriteria == "tenggat":
        tugas_list.sort(key=lambda x: datetime.strptime(x[2], "%d/%m/%Y"))
    elif kriteria == "prioritas":
        prioritas_urutan = {"Tinggi": 1, "Sedang": 2, "Rendah": 3}
        tugas_list.sort(key=lambda x: prioritas_urutan[x[4]])
    else:
        print("Kriteria tidak valid.")
        return

    print("Tugas berhasil diurutkan.")
    tampilkan_daftar_tugas(tugas_list)

# Program utama
def main():
    tugas_list = []
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_tugas(tugas_list)
        elif pilihan == "2":
            tampilkan_daftar_tugas(tugas_list)
        elif pilihan == "3":
            edit_tugas(tugas_list)
        elif pilihan == "4":
            hapus_tugas(tugas_list)
        elif pilihan == "5":
            cari_tugas(tugas_list)
        elif pilihan == "6":
            urutkan_tugas(tugas_list)
        elif pilihan == "7":
            tampilkan_statistik_tugas(tugas_list)
        elif pilihan == "8":
            print("Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")

# Menjalankan program
if __name__ == "__main__":
    main()
