import time
from app.modules.module_1.implementations import (
    Base1SubClass1, Base1SubClass2
)

from app.modules.module_2.implementations import (
     ElectricityMeter, WaterMeter, GasMeter
)
from app.modules.module_2.demo import run_demo as run_module_2_demo

# Modül 3'ün gerçek sınıflarını import edelim
from app.modules.module_3.implementations import (
    AmbulanceUnit, PoliceUnit, FireFightingUnit,
    Criminal, Victim,
    Hospital, PoliceStation, FireStation
)



def run_demo():
    while True:
        print("\n" + "="*60)
        print("🚨 AKILLI ACİL DURUM YÖNETİM SİSTEMİ - ANA MENÜ")
        print("="*60)
        print("📚 PROJE MODÜL SEÇİCİ")
        print("-"*60)
        
        print("\n📦 MEVCUT MODÜLLER:")
        print(" [1] 📊 Modül 1 - Öğrenci 1 Projesi")
        print(" [2] 🏙️ Modül 2 - Akıllı Şehir Altyapı Sistemi")
        print(" [3] 🚨 Modül 3 - Akıllı Acil Durum Yönetim Sistemi")
        print(" [4] 📈 Modül 4 - Öğrenci 4 Projesi")
        print(" [Q] ❌ Çıkış")
        print("-"*60)
        
        choice = input("👉 Seçiminiz (1-4, Q): ").upper()
        
        if choice == "1":
            print("\n" + "="*40)
            print("📊 MODÜL 1 - ÖĞRENCİ 1 PROJESİ")
            print("="*40)
            base_1 = [
                Base1SubClass1("parametre1"),
                Base1SubClass2("parametre2")
            ]
            for n in base_1:
                n.method1()
            input("\nDevam etmek için Enter'a basın...")
            
        elif choice == "2":
            print("\n" + "="*40)
            print("🏙️ MODÜL 2 - AKILLI ŞEHİR ALTYAPI SİSTEMİ")
            print("="*40)
            run_module_2_demo()
            input("\nDevam etmek için Enter'a basın...")
            
        elif choice == "3":
            print("\n" + "="*40)
            print("🚨 MODÜL 3 - AKILLI ACİL DURUM YÖNETİM SİSTEMİ")
            print("="*40)
            
            # Modül 3'ün kendi demo.py dosyasını çalıştır
            try:
                from app.modules.module_3.demo import main as run_module_3_demo
                run_module_3_demo()
            except ImportError as e:
                print(f"[HATA] Modül 3 demo'su yüklenemedi: {e}")
            
        
            
        elif choice == "Q":
            print("\n" + "="*40)
            print("👋 Sistemden çıkılıyor...")
            print("İyi çalışmalar!")
            print("="*40)
            break
            
        else:
            print("[HATA] Geçersiz seçim! Lütfen 1-4 arası bir sayı veya Q girin.")
            time.sleep(1)

if __name__ == "__main__":
    run_demo()