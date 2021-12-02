'''
Use the Vehicle class of the previous exercise (6). Add the following methods to the class:

- a method that takes as argument a tuple of two numbers and updates the velocity of the car to the input argument.
- a method that prints all the attributes of the car
- a method called "emissions". This method takes as argument a number (the distance travelled) and returns
  the amount of emissions produced by the Vehicle for that distance. If the vehicle is a non electric car
  the method will return 10 * distance, if the vehicle is a non electric truck, the  method will return 50 * distance. 
  If the vehicle is an electric car, the method will return 1 * distance and if the vehicle is an electric truck,
  the method will return 5 * distance. 

Weight: 2
'''

import numpy as np


class Vehicle:
    def __init__(self, type: str, velocity: tuple, colour:str, electric:bool):

        if type != "Car" and type != "Truck":
            print("Vehicle type must be a Car or Truck")

        self.type = type
        self.velocity = np.array(velocity)
        self.colour = colour
        self.electric = electric

    def updateVelocity(self, newVelocity: tuple):
      self.velocity = np.array(newVelocity)

    def attributes(self):
      print(f"Vehicle type:{self.type}, Vehicle velocity:{self.velocity}, Vehicle colour:{self.colour}, Vehicle is electric?:{self.electric}")

    def emissions(self, distance:float):
      if self.electric == False and self.type == "Car":
        return(10*distance)
      elif self.electric == False and self.type == "Truck":
        return(50*distance)
      elif self.electric ==True and self.type =="Car":
        return(distance)
      elif self.electric ==True and self.type =="Truck":
        return(5*distance)

      

# example to check code works
v1 = Vehicle("Car", (3,4), "Blue", False)

print(v1.velocity)
v1.updateVelocity((9,7))
print(v1.velocity)

v1.attributes()
print(v1.emissions(10))






