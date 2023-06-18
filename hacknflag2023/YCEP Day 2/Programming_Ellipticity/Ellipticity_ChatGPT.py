import random

class PathCalculator:
    def __init__(self):
        # Stdin values
        self.total_cities = 0  # Cities are the equivalent of nodes
        self.total_highways = 0  # Highways are the equivalent of edges
        self.all_ratings = []  # Where each rating is formatted as follows: {city name: security rating}
        self.all_highways = []  # Where each highway is formatted as follows: [city A, city B, travel time]
        self.distances = {}  # Store the shortest distances from start_city to each city
        self.previous = {}  # Store the previous city in the shortest path from start_city
        self.visited = set()  # Keep track of visited cities

        self.start_city = 0
        self.destination = 0

    def new_city(self, city_name, security_rating):
        self.all_ratings.append([city_name, security_rating])
        return 0

    def new_highway(self, start, end, travel_time):
        self.all_highways.append([start, end, travel_time])
        return 0

    def dijkstra_algorithm(self):
        self.distances[self.start_city] = 0

        while self.visited != set(range(1, self.total_cities + 1)):
            # Find the city with the smallest distance from the start_city
            unvisited_cities = {city for city in range(1, self.total_cities + 1)} - self.visited
            current_city = min(unvisited_cities, key=lambda city: self.distances.get(city, float('inf')))

            # Get the neighboring cities and their travel times
            neighbors = self.get_neighbors(current_city)

            for neighbor, travel_time in neighbors:
                distance = self.distances.get(current_city, float('inf')) + travel_time
                if distance < self.distances.get(neighbor, float('inf')):
                    self.distances[neighbor] = distance
                    self.previous[neighbor] = current_city

            self.visited.add(current_city)

        path = self.get_shortest_path()
        return path

    def get_neighbors(self, target_city: int) -> list:
        response = []
        for highway in self.all_highways:
            if highway[0] == target_city:
                response.append((highway[1], highway[2]))
        return response

    def get_shortest_path(self):
        path = []
        city = self.destination
        while city != self.start_city:
            path.append(city)
            city = self.previous[city]
        path.append(self.start_city)
        path.reverse()
        return path

def initialize():
    path_calculator = PathCalculator()
    path_calculator.total_cities = 8

    for i in range(1, path_calculator.total_cities + 1):
        path_calculator.new_city(i, random.randint(1, 2))

    path_calculator.new_highway(1, 2, 1)
    path_calculator.new_highway(1, 3, 1)
    path_calculator.new_highway(2, 4, 1)
    path_calculator.new_highway(4, 3, 1)
    path_calculator.new_highway(4, 5, 1)
    path_calculator.new_highway(4, 7, 1)
    path_calculator.new_highway(8, 5, 1)
    path_calculator.new_highway(8, 7, 1)
    path_calculator.new_highway(6, 2, 1)
    path_calculator.new_highway(6, 7, 1)

    path_calculator.start_city = 1
    path_calculator.destination = 5

    shortest_path = path_calculator.dijkstra_algorithm()
    print("Shortest Path:", shortest_path)

initialize()
