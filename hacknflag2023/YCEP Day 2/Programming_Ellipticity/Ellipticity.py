import pathfinding
import random

class PathCalculator():
    def __init__(self):
        # Stdin values
        self.total_cities = 0 # Cities are the equivalent of nodes
        self.total_highways = 0 # Highways are the equivalent of edges
        self.all_ratings = [] # Where each rating is formatted as follows: {city name: security rating}
        self.all_highways = [] # Where each highway is formatted as follows: [city A, city B, travel time]

        self.start_city = 0
        self.destination = 0
        self.current_city = -1

    def new_city(self, city_name, security_rating):
        self.all_ratings.append([city_name, security_rating])
        return 0

    def new_highway(self, start, end, travel_time):
        self.all_highways.append([start, end, travel_time])
        return 0

    def get_start_end(self):
        self.start_city = self.all_ratings[0][0]
        self.destination = self.all_ratings[-1][0]
        self.current_city = self.start_city
        return 0

    def get_paths(self, target_city: int) -> list:
        response = []
        for i in range(len(self.all_highways)):
            if self.all_highways[i][0] == target_city:
                response.append(self.all_highways[i])
            else:
                pass
        return response if response else None
    
    def dijkstra_algorithm(self) -> int | float:
        self.get_start_end() # Initialize the start and end points for the algorithm
        print(self.start_city, self.destination)
        paths_found = self.get_paths(self.start_city)
        while paths_found:
            print(len(paths_found))
            for i in range(len(paths_found)):
                self.current_city += 1
                paths_found = self.get_paths(self.current_city)
    

def main():
    path_calculator = PathCalculator()
    path_calculator.total_cities = int(input("Enter the number of accessible cities: "))
    path_calculator.total_highways = int(input("Enter the number of accessible highways: "))
    for i in range(path_calculator.total_cities):
        start_hrs = int(input(f"Enter the Hacker Rating System of the {i} city: "))
        path_calculator.all_ratings[i] = start_hrs
    for i in range(path_calculator.total_highways):
        new_highway = [input("Enter the first city: "), input("Enter the second city: "), input("Enter the travel time (in ms): ")]
        path_calculator.all_highways.append(new_highway)
    fastest_path = path_calculator.dijkstra_algorithm()
    print(f"Shortest time required: {fastest_path[0]}")
    print(f"Highest possible security: {fastest_path[1]}")

def test():
    path_calculator = PathCalculator()
    for i in range(1, 9):
        path_calculator.new_city(i, random.randint(1, 2))
    path_calculator.new_highway(1, 2, 1)
    path_calculator.new_highway(1, 3, 1)
    path_calculator.new_highway(2, 4, 1)
    path_calculator.new_highway(3, 4, 1)
    path_calculator.new_highway(4, 5, 1)
    path_calculator.new_highway(4, 7, 1)
    path_calculator.new_highway(5, 8, 1)
    path_calculator.new_highway(7, 8, 1)
    path_calculator.new_highway(6, 2, 1)
    path_calculator.new_highway(6, 7, 1)
    # path_calculator.get_start_end()
    # print(path_calculator.get_paths(1))
    path_calculator.dijkstra_algorithm()

if __name__ == "__main__":
    #main()
    test()