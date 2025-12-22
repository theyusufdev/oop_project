from abc import ABC, abstractmethod

class EmergencyUnit(ABC):
    total_fleet_count = 0

    def __init__(self, unit_id, unit_type, current_location, availability, fuel_level, is_enough_staff, is_siren_on = False, is_it_on_duty = False, max_fuel_level = 50):
        self.__unit_id = unit_id
        self.__unit_type = unit_type
        self.__current_location = current_location
        self.__availability = availability
        self.__fuel_level = fuel_level
        self.__is_enough_staff = is_enough_staff
        self.__is_siren_on = is_siren_on
        self.__is_it_on_duty = is_it_on_duty
        self.__max_fuel_level = max_fuel_level
        EmergencyUnit.total_fleet_count +=1

    @property
    def unit_id(self):
        return self.__unit_id
    
    @unit_id.setter
    def unit_id(self, new_id):
        self.__unit_id = new_id

    @property
    def unit_type(self):
        return self.__unit_type
    
    @unit_type.setter
    def unit_type(self, new):
        self.__unit_type = new

    @property
    def current_location(self):
        return self.__current_location
    
    @current_location.setter
    def current_location(self, new_locate):
        self.__current_location = new_locate


    @property
    def availability(self):
        return self.__availability
    
    @availability.setter
    def availability(self, status):
        self.__availability = status

    @property
    def fuel_level(self):
        return self.__fuel_level
    
    @fuel_level.setter
    def fuel_level(self, level):
        self.__fuel_level = level

    @property
    def is_enough_staff(self):
        return self.__is_enough_staff
    
    @is_enough_staff.setter
    def is_enough_staff(self, status):
        self.__is_enough_staff = status

    @property
    def is_siren_on(self):
        return self.__is_siren_on
    
    @is_siren_on.setter
    def is_siren_on(self, status):
        self.__is_siren_on = status

    @property
    def is_it_on_duty(self):
        return self.__is_it_on_duty
    
    @is_it_on_duty.setter
    def is_it_on_duty(self, status):
        self.__is_it_on_duty = status

    @property
    def max_fuel_level(self):
        return self.__max_fuel_level
    
    @max_fuel_level.setter
    def max_fuel_level(self, level):
        self.__max_fuel_level = level

    @abstractmethod
    def update_location(self):
        # Birimin konumunu günceller
        pass

    @abstractmethod
    def open_siren(self):
        # Birimin sirenini açar
        pass

    @abstractmethod
    def report_location(self):
        # Birimin konumunu bildirir
        pass
    
    @abstractmethod
    def report_accident(self):
        # Birimin arıza bildirimini yapar
        pass

    @abstractmethod
    def determine_availability(self):
        # Birimin müsaitlik durumunu belirler
        pass

    @abstractmethod
    def get_detailed_status(self):
        # Birime özel araç kimlik kartı oluşturur
        pass
    
    @abstractmethod
    def refill_tank(self):
        # Birimim depolarını doldurur
        pass

    @classmethod
    def show_fleet_summary(cls):
        return f"[SİSTEM] Şu an envanterde toplam {cls.total_fleet_count} adet araç kayıtlıdır."