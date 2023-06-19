# Temperature script

import sys

def temp_func(temp):
    if temp > 80:
        temp = "Too hot"
    elif temp < 65:
        temp = "Too cold"
    else:
        temp = "Quite nice"
    return temp

temp = int(sys.argv[1])

print(temp_func(temp))

