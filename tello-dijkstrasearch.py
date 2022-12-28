import random
import pytello

# Connect to the Tello drone
drone = pytello.Tello()

# Set the flight speed to 50 cm/s
drone.set_speed(50)

# Take off and hover at 1 meter above the ground
drone.takeoff()
drone.up(100)

# Create a random map as a 2D grid of integers, with 0 representing open space
# and 1 representing an obstacle
map_size = (10, 10)
map = [[random.randint(0, 1) for j in range(map_size[1])] for i in range(map_size[0])]

# Initialize the search algorithm
start = (0, 0)  # Start at the top left corner of the map
goal = (map_size[0] - 1, map_size[1] - 1)  # Goal is at the bottom right corner of the map
came_from, _, a_star_dis =  pytello.dijkstra.dijkstra(map, start, goal)

# Follow the path from the start to the goal
current = goal
while current != start:
    # Move the drone to the next position in the path
    next = came_from[current]
    drone.go(next[0] - current[0], next[1] - current[1], 0, 0)
    current = next

# Land and close the connection to the drone
drone.land()
drone.close()
