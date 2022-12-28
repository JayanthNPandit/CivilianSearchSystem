import random
import airsim

# Connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)

# Take off and hover at 1 meter above the ground
client.takeoffAsync().join()
client.moveToZAsync(1, velocity=5).join()

# Create a random map as a 2D grid of integers, with 0 representing open space
# and 1 representing an obstacle
map_size = (10, 10)
map = [[random.randint(0, 1) for j in range(map_size[1])] for i in range(map_size[0])]

# Initialize the search algorithm
start = (0, 0)  # Start at the top left corner of the map
goal = (map_size[0] - 1, map_size[1] - 1)  # Goal is at the bottom right corner of the map
came_from, _, a_star_dis =  airsim.dijkstra.dijkstra(map, start, goal)

# Follow the path from the start to the goal
current = goal
while current != start:
    # Move the drone to the next position in the path
    next = came_from[current]
    client.moveToPositionAsync(next[0], next[1], 1, velocity=5).join()
    current = next

# Land and disable API control
client.landAsync().join()
client.enableApiControl(False)
