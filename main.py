from easytello import tello

drone = tello.Tello()

# Function declerations
def scan():
    return 0;

def clear_path():
    pass

# Finds path and turns towards it
drone.takeoff()
degree = scan()
drone.cw(degree)

# Path traversing
while clear_path():
    drone.forward(100)
    deg = scan()
    drone.ccw(deg)

drone.land()