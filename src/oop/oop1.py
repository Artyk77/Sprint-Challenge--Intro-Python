# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# YOUR CODE HERE

class Vehicle: #base class

    def __init__(self, vehicle, flight_vehicle, ground_vehicle, car, motorcycle, starship, airplane):
        self.vehicle = Vehicle
        self.flight_vehicle = FlightVehicle
        self.ground_vehicle = GroundVehicle
        self.car = Car
        self.motorcycle = Motorcycle
        self.starship = Starship
        self.airplane = Airplane

class Craftever(Vehicle):

    def __init__(self, body, vehicle, flight_vehicle, ground_vehicle, car, motorcycle, starship, airplane):
        super().__init__(vehicle, flight_vehicle, ground_vehicle, car, motorcycle, starship, airplane)
        self.name = body

    def __str__(self):
        return 'Craftever { body = '+self.body+', vehicle = '+str(self.vehicle)+', flight_vehicle = '+str(self.flight_vehicle)+', ground_vehicle = '+str(self.ground_vehicle)+', car = '+str(self.car)+', motorcycle = '+str(self.motorcycle)+', starship = '+str(self.startship)+', airplane = '+str(self.airplane)+'}'