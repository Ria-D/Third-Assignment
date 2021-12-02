'''
Using the vehicle class that you created in the previous exercises, create 200 objects vehicle.
50 of them will be electric cars, 50 of them will be non electric cars. 50 of them will be electric trucks and
50 of them will be non electric trucks. The attribute velocity will be initialised randomly (with a positive number).

Write a function that takes as arguments a list of vehicles and a positive real number t (that represents time). The function will output the average 
emission for each category of vehicles (so, 4 averages, electric and non electric cars and trucks).

Notice that the velocity of each vehicle is expressed in terms of x and y component and you need to compute the total distance travelled.

hint: divide this exercise in subproblems and write appropriate functions for each subproblem

Weight: 3
'''
import numpy as np


class Vehicle:
    def __init__(self, type: str, velocity: tuple, electric:bool):

        if type != "Car" and type != "Truck":
            print("Vehicle type must be a Car or Truck")

        self.type = type
        self.velocity = np.array(velocity)
        self.electric = electric

    def emissions(self, distance:float):
      if self.electric == False and self.type == "Car":
        return(10*distance)
      elif self.electric == False and self.type == "Truck":
        return(50*distance)
      elif self.electric ==True and self.type =="Car":
        return(distance)
      elif self.electric ==True and self.type =="Truck":
        return(5*distance)

import random
electricCars = []
for i in range(50):
  electricCars.append(Vehicle("Car", (random.randint(1,100),random.randint(1,100)), True))

nonElectricCars= []
for i in range(50):
  nonElectricCars.append(Vehicle("Car", (random.randint(1,100),random.randint(1,100)), False))

electricTrucks= []
for i in range(50):
  electricTrucks.append(Vehicle("Truck", (random.randint(1,100),random.randint(1,100)), True))

nonElectricTrucks= []
for i in range(50):
  nonElectricTrucks.append(Vehicle("Truck", (random.randint(1,100),random.randint(1,100)), False))

def avgEmission(list1, time:int):
    
    sumEmission = 0
    for item in list1:
        distanceTravelled = (np.linalg.norm(item.velocity))*time
        sumEmission += item.emissions(distanceTravelled)
    averageEmission = sumEmission/50

    return(averageEmission)

print(avgEmission(electricCars, 10))
print(avgEmission(nonElectricCars, 10))
print(avgEmission(electricTrucks, 10))
print(avgEmission(nonElectricTrucks, 10))

        
        


