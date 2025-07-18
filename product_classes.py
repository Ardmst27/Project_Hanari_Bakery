# File: product_classes.py

from abc import ABC, abstractmethod

# =================================================
# SECTION 1: INTERFACE & ABSTRACT CLASS DEFINITIONS
# =================================================

class BisaMengembang(ABC):
    """Interface untuk produk yang memerlukan proses pengembangan."""
    @abstractmethod
    def pengembangan(self):
        pass

class PerluTopping(ABC):
    """Interface untuk produk yang memerlukan proses topping."""
    @abstractmethod
    def topping(self):
        pass

class ProdukRoti(ABC):
    """Abstract base class untuk semua produk bakery."""
    
    def __init__(self, kode: str, nama: str, biaya_produksi: float, harga_jual: float):
        self.kode = kode
        self.nama = nama
        self.biaya_produksi = biaya_produksi
        self.harga_jual = harga_jual

    @abstractmethod
    def tampilkan_info(self):
        """Menampilkan informasi lengkap dari produk."""
        pass
    
    # Proses umum yang dimiliki hampir semua produk
    def pengadonan(self):
        print(f"[{self.nama}] Melakukan proses pengadonan bahan baku...")

    def pemanggangan(self):
        print(f"[{self.nama}] Melakukan proses pemanggangan di oven...")

class RotiManis(ProdukRoti, BisaMengembang, PerluTopping):
    """Class untuk produk Roti Manis."""
    
    def __init__(self, kode: str = "RM001", nama: str = "Roti Manis", biaya_produksi: float = 3500.0, harga_jual: float = 8000.0):
        super().__init__(kode, nama, biaya_produksi, harga_jual)

    def tampilkan_info(self):
        return f"Produk: {self.nama} ({self.kode}) | Harga: Rp {self.harga_jual:,.2f}"

    def pengembangan(self):
        print(f"[{self.nama}] Adonan sedang diistirahatkan agar mengembang sempurna.")

    def topping(self):
        print(f"[{self.nama}] Menambahkan topping keju dan cokelat.")

class Croissant(ProdukRoti, BisaMengembang):
    """Class untuk produk Croissant."""
    
    def __init__(self, kode: str = "CR001", nama: str = "Croissant", biaya_produksi: float = 4000.0, harga_jual: float = 12000.0):
        super().__init__(kode, nama, biaya_produksi, harga_jual)
    
    def tampilkan_info(self):
        return f"Produk: {self.nama} ({self.kode}) | Harga: Rp {self.harga_jual:,.2f}"

    def pengembangan(self):
        print(f"[{self.nama}] Adonan croissant sedang melalui proses laminasi dan pengembangan.")

class ButterCookies(ProdukRoti, PerluTopping):
    """Class untuk Butter Cookies."""
    
    def __init__(self, kode: str = "BC001", nama: str = "Butter Cookies", biaya_produksi: float = 2500.0, harga_jual: float = 6000.0):
        super().__init__(kode, nama, biaya_produksi, harga_jual)

    def tampilkan_info(self):
        return f"Produk: {self.nama} ({self.kode}) | Harga: Rp {self.harga_jual:,.2f}"

    def topping(self):
        print(f"[{self.nama}] Menaburkan gula halus di atas cookies.")

class Muffin(ProdukRoti, PerluTopping):
    """Class untuk Muffin."""
    
    def __init__(self, kode: str = "MF001", nama: str = "Muffin", biaya_produksi: float = 3000.0, harga_jual: float = 7500.0):
        super().__init__(kode, nama, biaya_produksi, harga_jual)
    
    def tampilkan_info(self):
        return f"Produk: {self.nama} ({self.kode}) | Harga: Rp {self.harga_jual:,.2f}"

    def topping(self):
        print(f"[{self.nama}] Menambahkan choco chips sebagai topping.")