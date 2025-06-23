# File: product_classes.py

from abc import ABC, abstractmethod

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
    
    def __init__(self):
        super().__init__(
            kode="RM001",
            nama="Roti Manis",
            biaya_produksi=3500.0,
            harga_jual=8000.0
        )

    def tampilkan_info(self):
        return f"Produk: {self.nama} ({self.kode}) | Harga: Rp {self.harga_jual:,.2f}"

    def pengembangan(self):
        print(f"[{self.nama}] Adonan sedang diistirahatkan agar mengembang sempurna.")

    def topping(self):
        print(f"[{self.nama}] Menambahkan topping keju dan cokelat.")

class Croissant(ProdukRoti, BisaMengembang):
    """Class untuk produk Croissant."""
    
    def __init__(self):
        super().__init__(
            kode="CR001",
            nama="Croissant",
            biaya_produksi=4000.0,
            harga_jual=12000.0
        )
    
    def tampilkan_info(self):
        return f"Produk: {self.nama} ({self.kode}) | Harga: Rp {self.harga_jual:,.2f}"

    def pengembangan(self):
        print(f"[{self.nama}] Adonan croissant sedang melalui proses laminasi dan pengembangan.")

class ButterCookies(ProdukRoti, PerluTopping):
    """Class untuk Butter Cookies."""
    
    def __init__(self):
        super().__init__(
            kode="BC001",
            nama="Butter Cookies",
            biaya_produksi=2500.0,
            harga_jual=6000.0
        )

    def tampilkan_info(self):
        return f"Produk: {self.nama} ({self.kode}) | Harga: Rp {self.harga_jual:,.2f}"

    def topping(self):
        print(f"[{self.nama}] Menaburkan gula halus di atas cookies.")

class Muffin(ProdukRoti, PerluTopping):
    """Class untuk Muffin."""
    
    def __init__(self):
        super().__init__(
            kode="MF001",
            nama="Muffin",
            biaya_produksi=3000.0,
            harga_jual=7500.0
        )
    
    def tampilkan_info(self):
        return f"Produk: {self.nama} ({self.kode}) | Harga: Rp {self.harga_jual:,.2f}"

    def topping(self):
        print(f"[{self.nama}] Menambahkan choco chips sebagai topping.")