# File: main.py 

from bakery_management import SistemProduksi
from product_classes import RotiManis, Croissant, ButterCookies, Muffin

class MenuInterface:
    """Interface untuk menu sistem"""
    
    def __init__(self):
        self.sistem = SistemProduksi()
        self.running = True
    
    def tampilkan_menu_utama(self):
        """Menampilkan menu utama"""
        # --- PERUBAHAN DIMULAI DI SINI ---
        print("\n" + "="*60)
        print("      SISTEM INFORMASI PRODUKSI HANARI BAKERY")
        print("                  (Versi 1.1)")  #<-- BARIS INI DITAMBAHKAN
        print("="*60)
        # --- PERUBAHAN SELESAI ---
        print("1. Tampilkan Semua Produk")
        print("2. Tambah Produk Baru (Custom)")
        print("3. Kalkulator Estimasi Profit")
        print("4. Simulasi Proses Produksi")
        print("5. Keluar")
        print("-"*60)
    
    def tambah_produk_menu(self):
        """Menu untuk menambah produk baru yang fungsional"""
        print("\n=== TAMBAH PRODUK BARU ===")
        try:
            print("Pilih tipe produk yang akan ditambah:")
            print("1. Roti Manis\n2. Croissant\n3. Butter Cookies\n4. Muffin")
            pilihan_tipe = input("Pilihan (1-4): ")

            kode = input("Masukkan Kode Produk Baru: ").upper() # Ditambahkan .upper() untuk konsistensi
            nama = input("Masukkan Nama Produk Baru: ")
            biaya_produksi = float(input("Masukkan Biaya Produksi per unit: "))
            harga_jual = float(input("Masukkan Harga Jual per unit: "))
            
            produk_baru = None
            if pilihan_tipe == '1':
                produk_baru = RotiManis(kode, nama, biaya_produksi, harga_jual)
            elif pilihan_tipe == '2':
                produk_baru = Croissant(kode, nama, biaya_produksi, harga_jual)
            elif pilihan_tipe == '3':
                produk_baru = ButterCookies(kode, nama, biaya_produksi, harga_jual)
            elif pilihan_tipe == '4':
                produk_baru = Muffin(kode, nama, biaya_produksi, harga_jual)
            else:
                print("Tipe produk tidak valid.")
                return

            if produk_baru:
                self.sistem.tambah_produk(produk_baru)

        except ValueError:
            print("Input biaya atau harga tidak valid! Harap masukkan angka.")
        except Exception as e:
            print(f"Terjadi error: {e}")

    def kalkulator_profit_menu(self):
        """Menu kalkulator profit"""
        print("\n=== KALKULATOR ESTIMASI PROFIT ===")
        self.sistem.tampilkan_semua_produk()
        
        try:
            kode_produk = input("\nMasukkan Kode Produk yang akan dihitung: ").upper()
            if self.sistem.cari_produk(kode_produk):
                jumlah = int(input("Masukkan jumlah produksi (pcs): "))
                self.sistem.hitung_estimasi_profit(kode_produk, jumlah)
            else:
                print("Produk dengan kode tersebut tidak ditemukan.")
        except ValueError:
            print("Input jumlah harus berupa angka!")
    
    def simulasi_produksi_menu(self):
        """Menu simulasi proses produksi"""
        print("\n=== SIMULASI PROSES PRODUKSI ===")
        self.sistem.tampilkan_semua_produk()
        
        kode_produk = input("\nMasukkan Kode Produk untuk disimulasikan: ").upper()
        self.sistem.simulasi_proses_produksi(kode_produk)
    
    def jalankan(self):
        """Menjalankan aplikasi"""
        while self.running:
            self.tampilkan_menu_utama()
            
            pilihan = input("Pilih menu (1-5): ")
            
            if pilihan == "1":
                self.sistem.tampilkan_semua_produk()
            elif pilihan == "2":
                self.tambah_produk_menu()
            elif pilihan == "3":
                self.kalkulator_profit_menu()
            elif pilihan == "4":
                self.simulasi_produksi_menu()
            elif pilihan == "5":
                print("\nTerima kasih telah menggunakan Sistem Hanari Bakery!")
                self.running = False
            else:
                print("Pilihan tidak valid! Silakan pilih 1-5.")
            
            if self.running:
                input("\nTekan Enter untuk melanjutkan...")
                
# teknik mainnnn
# -----------------------

if __name__ == "__main__":
    app = MenuInterface()
    app.jalankan()