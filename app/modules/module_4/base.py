from abc import ABC, abstractmethod

class SocialService(ABC):
    def __init__(self, service_id, name, target_group):
        self.service_id = service_id
        self.name = name
        self.target_group = target_group
        self.status = "pasif"

    @abstractmethod
    def uygunluk_kontrolu(self, vatandas):
        pass

    @abstractmethod
    def destek_hesapla(self):
        pass

    def aktif_et(self):
        self.status = "aktif"

    def pasif_et(self):
        self.status = "pasif"

    @classmethod
    def servis_tipi(cls):
        return cls.__name__

    @staticmethod
    def belediye_politikasi():
        return "Sosyal adalet ve eşit destek"
