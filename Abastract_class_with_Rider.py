""" #9.3 Create a User abastract class with Rider  """

from abc import ABC, abstractmethod
from datetime import datetime


class Ride_Sharing:
    def __init__(self,company_name) -> None:
        self.company_name = company_name
        self.drivers = []
        self.riders = []
        self.rides = []

    def add_drivers(self,driver):
        self.drivers.append(driver)

    def add_riders(self,rider):
        self.riders.append(rider)

    def __repr__(self) -> str:
        return f'{self.company_name} with riders :{len(self.riders)} and drivers: {len(self.drivers)}'

class User(ABC):
    def __init__(self,name,email,NID,):
        self.name = name
        self.email = email 
        #TODO: set id dynnamically
        self.__id = 0
        self.__wallet = 0
        self.__nid = NID

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    
class Rider(User):
    def __init__(self, name, email, NID,current_location,initial_amount): 
        self.current_ride = None
        self.wallet = initial_amount
        self.current_location = current_location
        super().__init__(name, email, NID)

    def update_location (self,current_location):
        self.current_location = current_location    

    def load_cash(self,amount):
        if amount >0:
         self.wallet += amount    

    def display_profile(self):
        print(f"Rider : with name {self.name} with Email {self.email}")

    def request_rider(self,ride_sharing,destination):

        if not self.current_ride: # jodi current_ride na thake
            rider_request = Rider_Request(self, destination)
            ride_matcht = Ride_matcht(ride_sharing.drivers) 
            ride = ride_matcht.find_driver(rider_request)
            self.current_ride = ride

    def show_current_ride(self):
        if self.current_ride:
            print(f"Current Ride Details: {self.current_ride}")
        else:
            print("No current ride")



"""  #9.4 Ride class to create a ride  """


class Driver(User):

    def __init__(self, name, email, NID,current_location) -> None:
        super().__init__(name, email, NID)
        self.current_location = current_location


    def display_profile(self):
        print(f"Driver name {self.name} and Email : {self.email}")

    def accept_ride(self,rider,ride):
        rider.current_ride = ride

class Ride:
    def __init__(self,start_location,end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.start_time = None
        self.end_time = None
        self.driver = None
        self.rider = None
        self.estimated_fare = None
    
    def set_deriver(self,driver):
        self.driver = driver

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self,amount):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare

    def __repr__(self) -> str:
        return f'Ride details. Started: {self.start_location} to {self.end_location}'
        


""" # 9.5 Ride matching and ride request class """

class Rider_Request: 
    def __init__(self,rider, end_location) -> None:
        self.rider = rider
        self.end_location = end_location
        
class Ride_matcht:
    def __init__(self,drivers) -> None:
        self.avillable_driver= drivers

    def find_driver(self,rider_request):
        
        if len(self.avillable_driver) > 0:
            driver = self.avillable_driver[0]
            ride = Ride(rider_request.rider.current_location,rider_request.end_location)
            driver.accept_ride(rider_request.rider,ride)
            return ride


""" # 9.6 Create vehicles and ride sharing class """

class Vahical(ABC):

    speed = {
        'Car' : 50,
        'Bike': 60,
        'CNG' : 15
    }

    def __init__(self,vahical_type,licence_plate,rate) -> None:
        self.vahical_type = vahical_type
        self.licence_plate = licence_plate
        self.rate = rate
        self.status = 'Avaliable'
    @abstractmethod
    def start_drive(self):
        pass

class Car(Vahical):
    def __init__(self, vahical_type, licence_plate, rate) -> None:
        super().__init__(vahical_type, licence_plate, rate)
    
    def start_drive(self):
        self.status = 'Unavaliable'

class Bike(Vahical):
    def __init__(self, vahical_type, licence_plate, rate) -> None:
        super().__init__(vahical_type, licence_plate, rate)

    def start_drive(self):
        self.status = 'Unavaliable'


# check the class intefration

niye_jao = Ride_Sharing('NIye Jao')
sakib = Rider("Sakib khan", 'sakib@khan.com', 1254, 'mohakhali', 1200)
niye_jao.add_riders(sakib)
kala_pakhi = Driver('kala pakhi', 'kala@sada.com', 5648, 'gulshan 1')
niye_jao.add_drivers(kala_pakhi)
print(niye_jao)
sakib.request_rider(niye_jao,'Uttara')
sakib.show_current_ride()

        
