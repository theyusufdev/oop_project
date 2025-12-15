from .implementations import GidaYardimi, BarinmaDestegi, EgitimDestegi
from .repository import SosyalHizmetRepository
from .services import SosyalHizmetServisi

repo = SosyalHizmetRepository()
servis = SosyalHizmetServisi(repo)

vatandas = {
    "ad": "Ali",
    "gelir": 8000,
    "evi_var_mi": False,
    "ogrenci_mi": True
}

hizmetler = [
    GidaYardimi(1, 1500),
    BarinmaDestegi(2, 5000),
    EgitimDestegi(3, 2000)
]

for hizmet in hizmetler:
    sonuc = servis.basvuru_olustur(vatandas, hizmet)
    print(sonuc)
