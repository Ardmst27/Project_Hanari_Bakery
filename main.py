# File: main.py

from bakery_management import HanariBakery
from product_classes import *

class MenuInterface:
    """Interface untuk menu sistem"""
    
    def __init__(self):
        self.sistem = SistemProduksi()
        self.running = True
    
    def tampilkan_menu_utama(self):
        """Menampilkan menu utama"""
        print("\n" + "="*60)
        print("      SISTEM INFORMASI PRODUKSI HANARI BAKERY")
        print("="*60)
        print("1. Tambah Produk Baru")
        print("2. Tampilkan Semua Produk")
        print("3. Kalkulator Estimasi Profit")
        print("4. Simulasi Proses Produksi")
        print("5. Keluar")
        print("-"*60)
    
    def tambah_produk_menu(self):
        """Menu untuk menambah produk baru"""
        print("\n=== TAMBAH PRODUK BARU ===")
        print("Fitur ini dapat dikembangkan untuk menambah produk custom")
        print("Saat ini tersedia produk default: Roti Manis, Croissant, Butter Cookies, Muffin")
    
    def kalkulator_profit_menu(self):
        """Menu kalkulator profit"""
        print("\n=== KALKULATOR ESTIMASI PROFIT ===")
        print("Pilih jenis produk:")
        
        kode_list = self.sistem.get_daftar_kode_produk()
        for i, kode in enumerate(kode_list, 1):
            produk = self.sistem.cari_produk(kode)
            print(f"{i}. {produk.nama} ({kode})")
        
        try:
            pilihan = int(input(f"\nMasukkan pilihan (1-{len(kode_list)}): ")) - 1
            if 0 <= pilihan < len(kode_list):
                kode_produk = kode_list[pilihan]
                jumlah = int(input("Masukkan jumlah produksi (pcs): "))
                self.sistem.hitung_estimasi_profit(kode_produk, jumlah)
            else:
                print("Pilihan tidak valid!")
        except ValueError:
            print("Input harus berupa angka!")
    
    def simulasi_produksi_menu(self):
        """Menu simulasi proses produksi"""
        print("\n=== SIMULASI PROSES PRODUKSI ===")
        print("Pilih jenis produk:")
        
        kode_list = self.sistem.get_daftar_kode_produk()
        for i, kode in enumerate(kode_list, 1):
            produk = self.sistem.cari_produk(kode)
            print(f"{i}. {produk.nama} ({kode})")
        
        try:
            pilihan = int(input(f"\nMasukkan pilihan (1-{len(kode_list)}): ")) - 1
            if 0 <= pilihan < len(kode_list):
                kode_produk = kode_list[pilihan]
                self.sistem.simulasi_proses_produksi(kode_produk)
            else:
                print("Pilihan tidak valid!")
        except ValueError:
            print("Input harus berupa angka!")
    
    def jalankan(self):
        """Menjalankan aplikasi"""
        while self.running:
            self.tampilkan_menu_utama()
            
            try:
                pilihan = input("Pilih menu (1-5): ")
                
                if pilihan == "1":
                    self.tambah_produk_menu()
                elif pilihan == "2":
                    self.sistem.tampilkan_semua_produk()
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
                    
            except KeyboardInterrupt:
                print("\n\nProgram dihentikan oleh user.")
                self.running = False
            except Exception as e:
                print(f"Terjadi error: {e}")

# Program utama
if __name__ == "__main__":
    print("Memulai Sistem Informasi Produksi Hanari Bakery...")
    app = MenuInterface()
    app.jalankan()