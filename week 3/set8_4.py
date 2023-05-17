class Vehicle:
    def __init__(self, name, max_speed, mileage, capacity): 
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity
   
    def fare(self):
        print("Name: {}, Max Speed: {}, Mileage: {}, Capacity: {}".format(self.name, self.max_speed, self.mileage, self.capacity))
        return self.capacity * 100
    
class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, capacity):
        super().__init__(name, max_speed, mileage, capacity)
    
    def fare(self):
        return super().fare()*1.10
       
n = input("Enter the name of vehicle: ")
speed = int(input("Enter the maximum speed of vehicle: "))
mil = int(input("Enter the mileage of vehicle: "))
capacity = int(input("Enter seating capacity of vehicle: "))

vehicle_1 = Vehicle("Scooty",50,30000,43)
print("Total fare: ",vehicle_1.fare())

bus_1 = Bus(n,speed,mil,capacity)
print("Total fare: ",bus_1.fare())
