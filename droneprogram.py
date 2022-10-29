from djitellopy import tello
from time import sleep

Drone = tello.Tello()
Drone.connect()

print(Drone.get_battery())

Drone.takeoff()

for i in range(3):
    Drone.go_xyz_speed(-30,-30,0,20)

Drone.land()

print("Done!")