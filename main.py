from app.modules.module_1.implementations import (
    Base1SubClass1, Base1SubClass2
)

from app.modules.module_2.implementations import (
    ElectricityMeter, WaterMeter, GasMeter
)

from app.modules.module_3.implementations import (
    AmbulanceUnit, PoliceUnit, FireFightingUnit
)

from app.modules.module_4.implementations import (
    GidaYardimi, BarinmaDestegi, EgitimDestegi
)

def run_demo():
    print("=== PROJECT MENU ===")

    # Ogrenci 1 (Modul 1)
    base_1 = [
        Base1SubClass1("parametre1"),
        Base1SubClass2("parametre2")
    ]
    for n in base_1:
        n.method1()

    # Ogrenci 2 (Modul 2)
    base_2 = [
        ElectricityMeter("E-100", 150, "Musteri A", voltage=220),
        WaterMeter("W-200", 25, "Musteri B"),
        GasMeter("G-300", 100, "Musteri C")
    ]
    for n in base_2:
        print(n.get_status())

        
    # Ogrenci 3 (Modul 3) - Acil Durum Birimleri
    ambulans = AmbulanceUnit(101, 80, True, 90, True)
    polis = PoliceUnit(201, 75, True, "Merkez")
    itfaiye = FireFightingUnit(301, 85, True, 5000, 3000)
    
    print("\n=== Acil Durum Birimleri ===")
    ambulans.report_status()
    print()
    polis.report_status()
    print()
    itfaiye.report_status()

    # Ogrenci 4 (Modul 4) - Sosyal Hizmetler
    gida_yardimi = GidaYardimi(1, 1500, 15)
    barinma_destegi = BarinmaDestegi(2, 5000, "daire")
    egitim_destegi = EgitimDestegi(3, 2000, "lise")
    
    print(f"\n{gida_yardimi}")
    print(f"{barinma_destegi}")
    print(f"{egitim_destegi}")
    
    # Örnek vatandaş
    vatandas = {"ad": "Ali Yılmaz", "gelir": 8000, "evi_var_mi": False, "ogrenci_mi": True}
    print(f"\nGıda Yardımı Uygunluk: {gida_yardimi.uygunluk_kontrolu(vatandas)}")
    print(f"Barınma Desteği Uygunluk: {barinma_destegi.uygunluk_kontrolu(vatandas)}")
    print(f"Eğitim Desteği Uygunluk: {egitim_destegi.uygunluk_kontrolu(vatandas)}")

if __name__ == "__main__":
    run_demo()