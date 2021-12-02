'''
In this folder you will find a subfolder with a file "Data points.txt".
- The first column of the text file provides a list of 1000 points related to sensor 1
- The second column of the text file provides a list of 1000 points related to sensor 2

Write a program that extracts data from the file and plot them using matplotlib.pyplot.
The data relative to both sensors need to be plotted in the same graph (they are both relative to the y axis),
using different colors.
Add the following label to the x axis: "Time [s]"
Add the following label to the y axis: "Force [N]"

Weight: 2
'''
import matplotlib.pyplot as plt

import os
os.chdir("Data")

sensor1= []
sensor2= []
Time = [t for t in range(1000)]

with open("Data points.txt", "r") as file:
    for line in file:
        if "-" in line:
            continue
        
        else:
            data = line.split('    ')

            sensor1.append(float(data[0]))
            sensor2.append(float(data[1]))

    plt.xlabel("Time (s)")
    plt.ylabel("Force (N)")

    plt.plot(Time, sensor1)
    plt.plot(Time, sensor2)

    plt.show()


    
