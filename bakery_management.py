# File: bakery_management.py

from product_classes import *
from typing import List

class SistemProduksi:
    """Class untuk mengelola sistem produksi bakery"""
    
    # REVISI: Memperbaiki kesalahan penulisan dari init menjadi _init_
    def _init_(self):
        self.produk_list: List[ProdukRoti] = [] 
        self.init_produk()
    
    def init_produk(self):
        """Inisialisasi produk-produk yang tersedia"""
        self.produk_list = [
            RotiManis(),
            Croissant(),
            ButterCookies(),
            Muffin()
        ]
    
    def tambah_produk(self, produk: ProdukRoti):
        """Menambahkan produk baru ke dalam daftar produk."""
        self.produk_list.append(produk)
        print(f"\nProduk '{produk.nama}' berhasil ditambahkan!")

    def tampilkan_semua_produk(self):
        """Menampilkan semua produk yang tersedia"""
        print("\n=== DAFTAR PRODUK HANARI BAKERY ===")
        print("-" * 50)
        if not self.produk_list:
            print("Belum ada produk yang terdaftar.")
        else:
            for i, produk in enumerate(self.produk_list, 1):
                print(f"{i}. {produk.tampilkan_info()}")
        print("-" * 50)

    def hitung_estimasi_profit(self, kode_produk: str, jumlah: int):
        """Menghitung estimasi profit untuk produk tertentu"""
        produk = self.cari_produk(kode_produk)
        if produk:
            profit = (produk.harga_jual - produk.biaya_produksi) * jumlah
            total_biaya = produk.biaya_produksi * jumlah
            total_pendapatan = produk.harga_jual * jumlah
            
            print("\n=== ESTIMASI PROFIT ===")
            print(f"Produk: {produk.nama}")
            print(f"Jumlah produksi: {jumlah} pcs")
            print(f"Total biaya produksi: Rp {total_biaya:,.2f}")
            print(f"Total pendapatan: Rp {total_pendapatan:,.2f}")
            print(f"Estimasi profit: Rp {profit:,.2f}")
        else:
            print(f"Produk dengan kode {kode_produk} tidak ditemukan!")

    def simulasi_proses_produksi(self, kode_produk: str):
        """Mensimulasikan proses produksi untuk produk tertentu"""
        produk = self.cari_produk(kode_produk)
        if produk:
            print(f"\n=== SIMULASI PROSES PRODUKSI: {produk.nama} ===")
         
            produk.pengadonan()
            
            if isinstance(produk, BisaMengembang):
                produk.pengembangan()
         
            produk.pemanggangan()
            
            if isinstance(produk, PerluTopping):
                produk.topping()

            print(f"=== SIMULASI SELESAI: {produk.nama} ===")
        else:
            print(f"Produk dengan kode {kode_produk} tidak ditemukan!")
    
    def cari_produk(self, kode: str) -> ProdukRoti: 
        """Mencari produk berdasarkan kode"""
        for produk in self.produk_list:
            if produk.kode == kode:
                return produk
        return None
    
    def get_daftar_kode_produk(self) -> List[str]:
        """Mengembalikan daftar kode produk yang tersedia"""
        return [produk.kode for produk in self.produk_list]