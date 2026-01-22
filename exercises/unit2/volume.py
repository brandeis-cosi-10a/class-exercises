pi = 22/7

def sphereStats(radius):    
    print("Radius is: ", radius)
    sphereVolume(radius)
    sphereArea(radius)

def sphereVolume(radius):
    print("volume is: ", (4/3)*(pi*radius**3))

def sphereArea(radius): 
    print("area is: ", 4*pi*radius**2)


radius = 4.5
sphereStats(radius)
radius = 10
sphereStats(radius)
radius = 8
sphereStats(radius)
