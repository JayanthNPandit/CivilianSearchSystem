import pytello

# Connect to the Tello drone
drone = pytello.Tello()

# Set the flight speed to 50 cm/s
drone.set_speed(50)

# Take off and hover at 1 meter above the ground
drone.takeoff()
drone.up(100)

# Fly in a search pattern
drone.left(50)
drone.forward(50)
drone.right(100)
drone.backward(50)
drone.left(100)

# Land and close the connection to the drone
drone.land()
drone.close()
