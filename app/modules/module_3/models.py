from abc import ABC, abstractmethod

# Suçlu ve kurban sınıflarının miras alaması için İnsan sınıfı
class Human(ABC):
    total_population = 0

    def __init__(self, id, name, lastname, age, blood_group, height, weight, is_alive):
        self.__id = id
        self.__name = name
        self.__lastname = lastname
        self.__age = age
        self.__blood_group = blood_group
        self.__height  = height
        self.__weight = weight
        self.__is_alive = is_alive
        # Bu sınıf her çağrıldığında popülasyon sayısı artıcak
        Human.total_population += 1

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, new):
        self.__id = new

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new):
        self.__name = new

    @property
    def lastname(self):
        return self.__lastname
    
    @lastname.setter
    def lastname(self, new):
        self.__lastname = new

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, new):
        self.__age = new

    @property
    def blood_group(self):
        return self.__blood_group
    
    @blood_group.setter
    def blood_group(self, new):
        self.__blood_group = new

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, new):
        self.__height = new

    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, new):
        self.__weight = new

    @property
    def is_alive(self):
        return self.__is_alive
    
    @is_alive.setter
    def is_alive(self, new):
        self.__is_alive = new

    @abstractmethod
    def report_status(self):
        pass

    @abstractmethod
    def get_role_description(self):
        pass

    @classmethod
    def get_population_count(cls):
        return f"Toplam İnsan Sayısı: {cls.total_population}"

    @staticmethod
    def calculate_bmi(weight, height):
        if height > 0:
            height_m = height / 100
            return weight / (height_m ** 2)
        return 0

class Criminal(Human):
    most_wanted_list = []

    def __init__(self, id, name, lastname, age, blood_group, height, weight, is_alive, criminal_history, danger_level, is_caught, kill_count, injured_count):
        super().__init__(id, name, lastname, age, blood_group, height, weight, is_alive, )
        self.__criminal_history = criminal_history
        self.__danger_level = danger_level
        self.__is_caught = is_caught
        self.__kill_count = kill_count
        self.__injured_count = injured_count
        
        if danger_level > 8:
            Criminal.add_to_most_wanted(f"{name} {lastname} | Yaş:{age} | Boy:{height} Kilo:{weight} | Öldürme sayısı : {kill_count}")
    
    @property
    def criminal_history(self):
        return self.__criminal_history
    
    @criminal_history.setter
    def criminal_history(self, new):
        self.__criminal_history = new

    @property
    def danger_level(self):
        return self.__danger_level
    
    @danger_level.setter
    def danger_level(self, new):
        self.__danger_level = new

    @property
    def is_caught(self):
        return self.__is_caught
    
    @is_caught.setter
    def is_caught(self, new):
        self.__is_caught = new

    @property
    def kill_count(self):
        return self.__kill_count
    
    @kill_count.setter
    def kill_count(self, new):
        self.__kill_count = new

    @property
    def injured_count(self):
        return self.__injured_count
    
    @injured_count.setter
    def injured_count(self, new):
        self.__injured_count = new

    def report_status(self):
        status = "Yakalandı" if self.__is_caught else "Firar"
        return f"[POLİS] Suçlu Durumu: {status} | Tehlike Seviyesi: {self.__danger_level}"

    # Kişi suç durumunu açıklar
    def get_role_description(self):
        if self.__kill_count > 0:
            return f"[POLİS] Cinayet faili"
        elif self.__injured_count > 0:
            return f"[POLİS] Adam yaralama faili"
        else:
            return f"[POLİS] Yasadışı aktivitelerin faili"

    # Suçluyu en çok arananlar listesine ekler
    @classmethod
    def add_to_most_wanted(cls, full_name):
        cls.most_wanted_list.append(full_name)
        return f"[POLİS] {full_name} en çok arananlar listesine eklendi"

    # Suçlunun suç seviyesini belirler
    @staticmethod
    def analyze_crime_severity(crime_type):
        severity_map = {
            "Hırsılık": 3,
            "Darp": 6,
            "Cinayet": 10,
            "Kundaklama": 8,
            "Ağır Yaralama": 7,
        }
        return severity_map.get(crime_type, 1)
    
    # Suçlu her yeni suç işlediğinde tehliye seviyesini arttırır
    def update_danger_level(self, crime_type):
        point = self.analyze_crime_severity(crime_type)        
        current_total = self.danger_level + point
        self.danger_level = current_total
        
        print(f"[POLİS] {crime_type} işlendi. Tehlike seviyesi +{point} arttı. (Tehlike Seviyesi: {self.danger_level})")

class Victim(Human):
    all_victims_registry = []

    def __init__(self, id, name, lastname, age, blood_group, height, weight, is_alive, degree_of_injury, the_person_who_injured, cause_of_injury, ):
        super().__init__(id, name, lastname, age, blood_group, height, weight, is_alive)
        self.__degree_of_injury = degree_of_injury
        self.__the_person_who_injured = the_person_who_injured
        self.__cause_of_injury = cause_of_injury

    @property
    def degree_of_injury(self):
        return self.__degree_of_injury
    
    @degree_of_injury.setter
    def degree_of_injury(self, new):
        self.__degree_of_injury = new

    @property
    def the_person_who_injured(self):
        return self.__the_person_who_injured
    
    @the_person_who_injured.setter
    def the_person_who_injured(self, new):
        self.__the_person_who_injured = new

    @property
    def cause_of_injury(self):
        return self.__cause_of_injury
    
    @cause_of_injury.setter
    def cause_of_injury(self, new): 
        self.__cause_of_injury = new

    # Kurban durumu
    def report_status(self):
        return f"[AMBULANS][YARALI DURUMU] Yaralanma Seviyesi: {self.__degree_of_injury}/10 | Neden: {self.__cause_of_injury}"

    # Kurban hakkında açıklama
    def get_role_description(self):
        return f"Kurban {self.__cause_of_injury} sebebiyle yaralı"

    # Kurbanın ailesine haber veriyoruz
    def notify_family(self, hospital_name):
        if not self.is_alive:
            message = f"[HASTAHANE] Başınız Sağolsun: {self.name} {self.lastname} isimli yakınınızı kaybettik. Lütfen {hospital_name} morguna geliniz."
        elif self.__degree_of_injury > 7:
            message = f"[HASTAHANE] Yakınınız {self.name}, {hospital_name} hastanesine kaldırıldı. Durumu KRİTİK. Acilen gelmeniz gerekiyor."
        else:
            message = f"[HASTAHANE] Yakınınız {self.name}, {hospital_name} hastanesinde müşahade altında. Durumu iyi, endişelenmeyin."
        
        # Durumu mesaj olarak hasta yakınlarına gönderir
        print(f"📨 [SMS GÖNDERİLDİ] -> {self.__family_contact}: {message}")
        return True
    
    # Sadece yaralı olan ve belli bir seviyenin üstündeki hastaların yakınlarına bilgilendirme yapar
    @classmethod
    def mass_notify_families(cls, min_severity=1):
        count = 0
        
        for victim in cls.all_victims_registry:
            if victim.is_alive and victim.degree_of_injury >= min_severity:
                victim.notify_family("Merkez Şehir Hastanesi")
                count += 1
        
        return f"[HASTAHANE] Toplam {count} ailenin telefonuna bilgilendirme mesajı gönderildi."

    # Yaralının yaşına ve yaralanma derecesine göre öncelik belirler
    @staticmethod
    def prioritize(degree_of_injury, age):
        score = degree_of_injury
        if age > 70 or age < 10:
            score += 2
        return score

class Structure(ABC):
    total_structures = 0

    def __init__(self, structure_id, name, address, capacity, current_occupancy, location):
        self.__structure_id = structure_id
        self.__name = name
        self.__address = address
        self.__capacity = capacity
        self.__current_occupancy = current_occupancy
        self.__location = location
        Structure.total_structures += 1

    @property
    def structure_id(self):
        return self.__structure_id

    @structure_id.setter
    def structure_id(self, new_id):
        self.__structure_id = new_id

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self, new_address):
        self.__address = new_address

    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, new_capacity):
        self.__capacity = new_capacity

    @property
    def current_occupancy(self):
        return self.__current_occupancy
    
    @current_occupancy.setter
    def current_occupancy(self, new_occupancy):
        self.__current_occupancy = new_occupancy

    @property
    def location(self):
        return self.__location
    
    @location.setter
    def location(self, new_loc):
        self.__location = new_loc

    @abstractmethod
    def calculate_maintenance_cost(self):
        pass

    @classmethod
    def get_total_structure_count(cls):
        return f"Toplam Bina Sayısı: {cls.total_structures}"

    # Konumu doğrular
    @staticmethod
    def validate_location(location):
        if 0 <= location <= 100:
            return True
        return False

class Hospital(Structure):
    pandemic_mode = False

    def __init__(self, structure_id, name, address, capacity, current_occupancy, location, number_of_doctors, number_of_ambulances, specialized_units):
        super().__init__(structure_id, name, address, capacity, current_occupancy, location)
        self.__number_of_doctors = number_of_doctors
        self.__number_of_ambulances = number_of_ambulances
        self.__specialized_units = specialized_units
        self.__patients_list = []

    @property
    def number_of_doctors(self):
        return self.__number_of_doctors
    
    @number_of_doctors.setter
    def number_of_doctors(self, count):
        self.__number_of_doctors = count

    @property
    def number_of_ambulances(self):
        return self.__number_of_ambulances
    
    @number_of_ambulances.setter
    def number_of_ambulances(self, count):
        self.__number_of_ambulances = count

    @property
    def specialized_units(self):
        return self.__specialized_units
    
    @specialized_units.setter
    def specialized_units(self, units):
        self.__specialized_units = units

    @property
    def patients_list(self):
        return self.__patients_list

    def add_patient(self, victim):
        if self.current_occupancy < self.capacity:
            self.__patients_list.append(victim)
            self.current_occupancy += 1
            return True
        return False

    # Hastahane bakım maliyetini hesaplar
    def calculate_maintenance_cost(self):
        base_cost = 5000
        doctor_cost = self.__number_of_doctors * 200
        return base_cost + doctor_cost

    @classmethod
    def set_pandemic_mode(cls, status):
        cls.pandemic_mode = status
        return f"[HASTAHANE] Pandemi durumu: {status}"

    # Kan grubu uyumunu kontrol eder
    @staticmethod
    def check_blood_compatibility(donor_type, recipient_type):
        if donor_type == "O Rh-":
            return True
        elif donor_type == recipient_type:
            return True
        return False

class PoliceStation(Structure):
    # Tüm birimlerin ciddiyet seviyesi
    severity = 3

    def __init__(self, structure_id, name, address, capacity, current_occupancy, location, cell_count, number_of_officers, patrol_cars_count):
        super().__init__(structure_id, name, address, capacity, current_occupancy, location)
        self.__cell_count = cell_count
        self.__number_of_officers = number_of_officers
        self.__patrol_cars_count = patrol_cars_count
        self.__criminals_in_custody = []

    @property
    def cell_count(self):
        return self.__cell_count
    
    @cell_count.setter
    def cell_count(self, count):
        self.__cell_count = count

    @property
    def number_of_officers(self):
        return self.__number_of_officers
    
    @number_of_officers.setter
    def number_of_officers(self, count):
        self.__number_of_officers = count

    @property
    def patrol_cars_count(self):
        return self.__patrol_cars_count
    
    @patrol_cars_count.setter
    def patrol_cars_count(self, count):
        self.__patrol_cars_count = count

    @property
    def criminals_in_custody(self):
        return self.__criminals_in_custody

    def book_criminal(self, criminal):
        if len(self.__criminals_in_custody) < self.__cell_count:
            self.__criminals_in_custody.append(criminal)
            self.current_occupancy += 1
            return True
        return False

    # Bina bakım maliyetini hesaplar
    def calculate_maintenance_cost(self):
        return (self.__number_of_officers * 100) + (self.__patrol_cars_count * 50)

    # Ülke genelinde polis birimlerinin ciddiyet seviyesini belirler
    @classmethod
    def change_severity_level(cls, level):
        if 1 <= level <= 5:
            cls.severity = level
            return f"[SİSTEM] Ülke genelinde tüm birimlerin ciddiyet seviyesi güncellendi: {level}"
        return "[SİSTEM] Geçerli bir seviye girin"
 
    # Kişinin serbest bırakılması için gerekli olan kefalet miktarını belirle
    @staticmethod
    def calculate_bail_amount(danger_level, crime_count):
        base_bail = 1000
        return base_bail * danger_level * (crime_count + 1)

class FireStation(Structure):
    # Binalarda olması gereken min su seviyesi (lt türünden)
    water_reserve_standard = 100000

    def __init__(self, structure_id, name, address, capacity, current_occupancy, location, number_of_engines, water_tank_capacity, foam_reserve):
        super().__init__(structure_id, name, address, capacity, current_occupancy, location)
        self.__number_of_engines = number_of_engines
        self.__water_tank_capacity = water_tank_capacity
        self.__foam_reserve = foam_reserve

    @property
    def number_of_engines(self):
        return self.__number_of_engines
    
    @number_of_engines.setter
    def number_of_engines(self, count):
        self.__number_of_engines = count

    @property
    def water_tank_capacity(self):
        return self.__water_tank_capacity
    
    @water_tank_capacity.setter
    def water_tank_capacity(self, capacity):
        self.__water_tank_capacity = capacity

    @property
    def foam_reserve(self):
        return self.__foam_reserve
    
    @foam_reserve.setter
    def foam_reserve(self, reserve):
        self.__foam_reserve = reserve

    # Binanın işleyiş maliyetini hesaplar
    def calculate_maintenance_cost(self):
        return (self.__number_of_engines * 300) + (self.__water_tank_capacity * 0.1) + (self.__foam_reserve * 0.4)

    # Olması gerekn min su seviyesini günceller
    @classmethod
    def update_water_standard(cls, new_standard):
        cls.water_reserve_standard = new_standard
        return f"[SİSTEM] Ülke geenelindeki itfaiye binlarında olması gereken su miktarı güncellendi: {new_standard}"

    # Suyun yangın yerine ulaşması için gereken pompa gücünü hesaplar
    @staticmethod
    def calculate_needed_pressure(height):
        return 2 + (height * 0.43)