'''
Write a class Vehicle, that takes in (via the constructor) the following attributes:

- type of the Vehicle (a string that can be either "Car" or "Truck")
- the velocity of the Vehicle (a tuple with two numbers, x and y)
- the color of the vehicle (a string)
- wheter or not the vehicle is electric (a boolean, True if it is an electric vehicle, False otherwise)

In the constructor argument, transform the tuple that you get as an input into a Numpy array.

Weight: 1
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

vehicle1 = Vehicle("bike", (3,4), "blue", False)   

    


