'''
In this folder you will find a subfolder with a file "Data points.txt".
- The first column of the text file provides a list of 1000 points related to sensor 1
- The second column of the text file provides a list of 1000 points related to sensor 2

Write a program that extracts data from the file and computes the average 
of the two measurements (for each row, the average between sensor 1 and sensor 2). 
You will end up with 1000 data points that you need to write in another text file called "Data points average.txt"

Weight: 2
'''

import os
os.chdir("Data")


newlist = []
with open("Data points.txt", "r") as file:
    

    for line in file:
        if "-" in line:
            continue
        
        else:
            data = line.split('    ')
        
        

            sumline = 0
            for number in data:
                sumline += float(number)
            
            averagenumber = (sumline/2)
        
            newlist.append(averagenumber)
        

f = open("Data points average.txt", "w")
for i in newlist:
    f.write(f" {str(i)} \n")        
        
f.close()
