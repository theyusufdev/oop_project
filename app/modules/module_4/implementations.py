from .base import SocialService

class GidaYardimi(SocialService):
    def __init__(self, service_id, aylik_tutar):
        super().__init__(service_id, "Gıda Yardımı", "Düşük Gelir")
        self.aylik_tutar = aylik_tutar

    def uygunluk_kontrolu(self, vatandas):
        return vatandas["gelir"] < 10000

    def destek_hesapla(self):
        return self.aylik_tutar


class BarinmaDestegi(SocialService):
    def __init__(self, service_id, kira_limiti):
        super().__init__(service_id, "Barınma Desteği", "Evsiz")
        self.kira_limiti = kira_limiti

    def uygunluk_kontrolu(self, vatandas):
        return vatandas["evi_var_mi"] is False

    def destek_hesapla(self):
        return self.kira_limiti


class EgitimDestegi(SocialService):
    def __init__(self, service_id, burs_miktari):
        super().__init__(service_id, "Eğitim Desteği", "Öğrenci")
        self.burs_miktari = burs_miktari

    def uygunluk_kontrolu(self, vatandas):
        return vatandas["ogrenci_mi"] is True

    def destek_hesapla(self):
        return self.burs_miktari
