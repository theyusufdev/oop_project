class SosyalHizmetRepository:
    def __init__(self):
        self.hizmetler = []
        self.basvurular = []

    def hizmet_ekle(self, hizmet):
        self.hizmetler.append(hizmet)

    def hizmetleri_getir(self):
        return self.hizmetler

    def basvuru_ekle(self, basvuru):
        self.basvurular.append(basvuru)

    def basvurulari_getir(self):
        return self.basvurular
