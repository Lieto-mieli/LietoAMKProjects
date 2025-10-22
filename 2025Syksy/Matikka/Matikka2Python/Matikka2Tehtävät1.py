import numpy as np
def rad(deg):
    return f"{np.radians(deg):.03f} rad  "
print(f"1. a. {np.degrees(2.493):.02f} °  b. {np.degrees(0.911):.02f} °")
print(f"2. a. {np.radians(137.7):.03f} rad  b. {np.radians(62.3):.03f} rad")
print("30°        45°        60°        90°        120°       135°       150°       180°       270°       360°       ")
print(rad(30)+rad(45)+rad(60)+rad(90)+rad(120)+rad(135)+rad(150)+rad(180)+rad(270)+rad(360))