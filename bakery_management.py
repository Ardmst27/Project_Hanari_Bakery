# File: bakery_management.py

from product_classes import *
from typing import List

class SistemProduksi:
    """Class untuk mengelola sistem produksi bakery"""
    
    def _init_(self):
        self.produk_list: List[Produk] = []
        self.init_produk()
    
    def init_produk(self):
        """Inisialisasi produk-produk yang tersedia"""
        self.produk_list = [
            RotiManis(),
            Croissant(),
            ButterCookies(),
            Muffin()
        ]
    
    def tambah_produk(self, produk: Produk):
        """Menambah produk baru ke sistem"""
        self.produk_list.append(produk)
        print(f"Produk {produk.nama} berhasil ditambahkan!")
    
    def tampilkan_semua_produk(self):
        """Menampilkan semua produk yang tersedia"""
        print("\n=== DAFTAR PRODUK HANARI BAKERY ===")
        print("-" * 50)
        for i, produk in enumerate(self.produk_list, 1):
            print(f"{i}. {produk.nama} ({produk.kode})")
            print(f"   Biaya Produksi: Rp {produk.biaya_produksi:,}")
            print(f"   Harga Jual: Rp {produk.harga_jual:,}")
            print(f"   Profit per unit: Rp {produk.harga_jual - produk.biaya_produksi:,}")
            print()
    
    def hitung_estimasi_profit(self, kode_produk: str, jumlah: int):
        """Menghitung estimasi profit untuk produk tertentu"""
        produk = self.cari_produk(kode_produk)
        if produk:
            profit = produk.hitung_profit(jumlah)
            total_biaya = produk.hitung_biaya_total(jumlah)
            total_pendapatan = produk.harga_jual * jumlah
            
            print("\n=== ESTIMASI PROFIT ===")
            print(f"Produk: {produk.nama}")
            print(f"Jumlah produksi: {jumlah} pcs")
            print(f"Total biaya produksi: Rp {total_biaya:,}")
            print(f"Total pendapatan: Rp {total_pendapatan:,}")
            print(f"Estimasi profit: Rp {profit:,}")
            
            return profit
        else:
            print(f"Produk dengan kode {kode_produk} tidak ditemukan!")
            return 0
    
    def simulasi_proses_produksi(self, kode_produk: str):
        """Mensimulasikan proses produksi untuk produk tertentu"""
        produk = self.cari_produk(kode_produk)
        if produk:
            print(f"\n=== SIMULASI PROSES PRODUKSI ===")
            print(f"Produk: {produk.nama}")
            print("Proses yang dibutuhkan:")
            
            proses_list = produk.get_proses_produksi()
            for i, proses in enumerate(proses_list, 1):
                print(f"{i}. {proses}")
            
            print(f"\nBahan baku yang dibutuhkan per unit:")
            for bahan, jumlah in produk.bahan_baku.items():
                print(f"- {bahan}: {jumlah} kg")
        else:
            print(f"Produk dengan kode {kode_produk} tidak ditemukan!")
    
    def cari_produk(self, kode: str) -> Produk:
        """Mencari produk berdasarkan kode"""
        for produk in self.produk_list:
            if produk.kode == kode:
                return produk
        return None
    
    def get_daftar_kode_produk(self) -> List[str]:
        """Mengembalikan daftar kode produk yang tersedia"""
        return [produk.kode for produk in self.produk_list]