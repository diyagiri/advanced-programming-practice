class Vehicle:
    def __init__(self, name, max_speed, mileage): 
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def __str__(self):
        return "Name: {}, Max Speed: {}, Mileage: {}".format(self.name, self.max_speed, self.mileage)

n = input("Enter the name of vehicle: ")
speed = int(input("Enter the maximum speed of vehicle: "))
mil = int(input("Enter the mileage of vehicle: "))

vehicle_1 = Vehicle(n,speed,mil)
print(vehicle_1)



