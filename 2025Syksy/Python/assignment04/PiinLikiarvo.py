import random
import math
pointsInCircle = 0
numOfPoints = int(input("How many points to calculate with?: "))
count = 0
while count < numOfPoints:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if (pow(x,2)+pow(y,2))<1:
        pointsInCircle+=1
    count += 1
print(f"pi =~ {4*pointsInCircle/numOfPoints}")