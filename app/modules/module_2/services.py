from .implementations import ElectricityMeter, WaterMeter, GasMeter
from datetime import datetime
import random

# Veritabanı simülasyonu için basit bir geçmiş listesi
USAGE_HISTORY = {}

class MeterService:
    """
    Sayaç yönetimini (oluşturma, arama, raporlama) sağlayan servis katmanı.
    """
    
    # Class Metot: Desteklenen sayaç tiplerini döndürür.
    @classmethod
    def get_supported_types(cls):
        """Servisin desteklediği sayaç tiplerini döndürür."""
        return ["Electricity", "Water", "Gas"]

    # Static Metot: Eşsiz ID üretir.
    @staticmethod
    def generate_unique_id(prefix="M"):
        """Sayaçlar için rastgele eşsiz ID üretir."""
        return f"{prefix}-{random.randint(1000, 9999)}"

    def __init__(self):
        # Sayaç nesnelerini tutan ana liste (repository simülasyonu)
        self._meters = []

    def register_meter(self, meter_type, usage, location):
        """Yeni bir sayaç oluşturur ve listeye ekler (Sayaç kaydı)."""
        meter_id = self.generate_unique_id(prefix=meter_type[0])
        
        if meter_type == "Electricity":
            new_meter = ElectricityMeter(meter_id, usage, location)
        elif meter_type == "Water":
            new_meter = WaterMeter(meter_id, usage, location)
        elif meter_type == "Gas":
            new_meter = GasMeter(meter_id, usage, location)
        else:
            raise ValueError(f"Bilinmeyen sayaç tipi: {meter_type}")

        self._meters.append(new_meter)
        USAGE_HISTORY[meter_id] = [] # Geçmiş kaydını başlat
        return new_meter

    def find_meter_by_location(self, location_keyword):
        """Lokasyon kelimesi içeren sayaçları bulur (Lokasyon bazlı arama)."""
        results = [
            meter for meter in self._meters 
            if location_keyword.lower() in meter.get_location().lower()
        ]
        return results

    def record_usage(self, meter_id, usage_delta):
        """Sayaç kullanımını günceller ve geçmişe kaydeder."""
        for meter in self._meters:
            if meter.get_id() == meter_id:
                current_usage = meter.get_usage_amount()
                new_usage = current_usage + usage_delta
                meter.set_usage_amount(new_usage)
                
                # Tüketim geçmişi saklama
                USAGE_HISTORY[meter_id].append({
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "delta": usage_delta,
                    "total": new_usage
                })
                
                # Aşırı Kullanım Tespiti
                if usage_delta > 100 and meter._type == "Electricity":
                    print(f"!!! Aşırı Kullanım Tespiti: {meter_id} için tek seferde 100 birim aşıldı.")

                return f"{meter_id} güncel tüketimi: {new_usage} birim."
        return f"Hata: {meter_id} bulunamadı."

    def simulate_failure(self, meter_type, location_keyword):
        """Belirtilen tip ve lokasyonda kesinti simülasyonu (Otomatik kesinti simülasyonu)."""
        affected_meters = [
            meter for meter in self._meters 
            if meter._type == meter_type and location_keyword.lower() in meter.get_location().lower()
        ]
        
        count = 0
        for meter in affected_meters:
            if hasattr(meter, 'simulate_power_cut'):
                meter.simulate_power_cut()
                count += 1
            elif hasattr(meter, 'check_leakage'):
                # Su sayacı için kaçak kontrolü
                meter.check_leakage()
                count += 1

        if count > 0:
            return f"{meter_type} tipinde {count} sayaçta kesinti/arıza simüle edildi."
        return "Belirtilen kriterlere uygun sayaç bulunamadı veya simülasyon metodu yok."


    def generate_report(self):
        """Tüm sayaçlar için özet rapor üretir (Rapor üretimi)."""
        report = "--- AKILLI ŞEHİR UTILITY RAPORU ---\n"
        total_cost = 0

        for meter in self._meters:
            cost = meter.calculate_cost()
            report += f"{meter.get_status()} | Fatura Tutar: {cost:.2f} TL\n"
            total_cost += cost

        report += f"\nTOPLAM GENEL MALİYET: {total_cost:.2f} TL"
        return report