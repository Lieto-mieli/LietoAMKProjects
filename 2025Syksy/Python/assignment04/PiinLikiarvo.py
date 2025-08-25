import random
pointsInCircle = 0
numOfPoints = int(input("How many points to calculate with?: "))
count = 0
while count < numOfPoints:
    x = random.randint(-1, 1)
    y = random.randint(-1, 1)
    if not (x^2+y^2)<1:
        pointsInCircle+=1
    count += 1
print(f"pi =~ {4*numOfPoints}")