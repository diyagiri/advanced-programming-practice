class Vehicle:
    def __init__(self, name, max_speed, mileage): 
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def seating_capacity(self, capacity):
        print("Name: {}, Max Speed: {}, Mileage: {}, Capacity: {}".format(self.name, self.max_speed, self.mileage, capacity))

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)
    
    def seating_capacity(self, capacity=50):
        super().seating_capacity(capacity)

n = input("Enter the name of vehicle: ")
speed = int(input("Enter the maximum speed of vehicle: "))
mil = int(input("Enter the mileage of vehicle: "))

vehicle_1 = Vehicle(n,speed,mil)
vehicle_1.seating_capacity(5)

bus_1 = Bus(n,speed,mil)
bus_1.seating_capacity() 
