# import random
class Car:
    def __init__(self, licensePlate, maxSpeed):
        self.license_plate = licensePlate
        self.maximum_speed = maxSpeed
        self.current_speed = 0
        self.travelled_distance = 0
    def __it__(self, other):
        return self.travelled_distance < other.travelled_distance
    def accelerate(self, nopeudenmuutos_kmh):
        self.current_speed += nopeudenmuutos_kmh
        self.current_speed = min(self.current_speed, self.maximum_speed)
        self.current_speed = max(self.current_speed, 0)
    def drive(self, matka_h):
        self.travelled_distance += matka_h*self.current_speed
class ElectricCar(Car):
    def __init__(self, licensePlate, maxSpeed, battery_capacity):
        super().__init__(licensePlate, maxSpeed)
        self.battery_capacity = battery_capacity
class GasolineCar(Car):
    def __init__(self, licensePlate, maxSpeed, tank_volume):
        super().__init__(licensePlate, maxSpeed)
        self.tank_volume = tank_volume
# class Race:
#     def __init__(self, name, length_km, participants_list):
#         self.name = name
#         self.distance = length_km
#         self.cars = participants_list
#         self.hour = 0
#     def hour_passes(self):
#         for o in self.cars:
#             o.accelerate(random.randint(-10,15))
#             o.drive(1)
#             if o.travelled_distance >= self.distance:
#                 finish = True
#         self.hour += 1
#     def print_status(self):
#         #print("")
#         #print(f"Contestant stats at Day {1+(self.hour//24)}, {self.hour%24}00 Hours: ")
#         for o in self.cars:
#             print(f"{o.license_plate}'s results:  Max Speed: {o.maximum_speed} km/h | Current speed: {o.current_speed} km/h | Distance travelled: {o.travelled_distance} km")
#     def race_finished(self):
#         finish = False
#         for o in self.cars:
#             if o.travelled_distance >= self.distance:
#                 finish = True
#         if finish:
#             return True
#         return False