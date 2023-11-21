class Elevator:
    def __init__(self, num_floors, capacity, floor_queues):
        # Initialize elevator properties
        self.num_floors = num_floors
        self.capacity = capacity
        self.floor_queues = floor_queues
        self.current_floor = 0
        # 1 for up, -1 for down
        self.direction = 1
        self.passengers = []
        # Flag variable to check if a stop was made to load or unload passengers
        self.stop_made = False

    def run_elevator(self):
        # Continue until there are no people waiting on any floor and no passengers inside
        while any(self.floor_queues) or len(self.passengers) > 0:
            self.stop_made = False
            self.unload_passengers()
            self.load_passengers()
            # If a stop was made, print information about the current state
            if self.stop_made:
                print(f"Stop at floor {self.current_floor}. People currently loaded: {len(self.passengers)}")
            self.choose_next_floor()
        print("Elevator has completed its operation. No more people waiting.")
        self.current_floor = 0

    def unload_passengers(self):
        # Check if there are passengers to unload
        if self.passengers:
            # Unload all passengers with the current floor as their destination
            new_passengers = [p for p in self.passengers if p != self.current_floor]
            # If unloading occurred, set stop_made flag to True
            if new_passengers != self.passengers:
                self.stop_made = True
            self.passengers = new_passengers

    def load_passengers(self):
        # Check if there are people waiting on the current floor
        if self.floor_queues[self.current_floor]:
            count = 0
            # Load passengers up to the elevator's capacity
            while count < len(self.floor_queues[self.current_floor]):
                person = self.floor_queues[self.current_floor][count]
                # Check if the person's direction aligns with the elevator's current direction
                if len(self.passengers) < self.capacity and (self.direction == 1 and person > self.current_floor
                            or self.direction == -1 and person < self.current_floor):
                    # Load the passenger into the elevator and remove them from the floor's queue
                    self.passengers.append(self.floor_queues[self.current_floor].pop(count))
                    self.stop_made = True
                else:
                    count += 1
                # If the elevator is at full capacity, break out of the loop
                if len(self.passengers) == self.capacity:
                    break

    def choose_next_floor(self):
        # Move to the next floor based on the current direction
        if (self.direction == 1 and self.current_floor < self.num_floors - 1
                or self.direction == -1 and self.current_floor > 0):
            self.current_floor += self.direction
        else:
            # Switch directions if at the top or bottom floor
            self.direction = -self.direction


def main():

    # Get elevator capacity from user input
    while True:
        elevator_capacity = int(input("Please input the elevator's capacity (at least one person): "))
        if elevator_capacity <= 0:
            print("Invalid input. The elevator's capacity should be at least one person")
        else:
            break

    # Get the number of floors from user input
    while True:
        num_floors = int(input("Please input number of floors (more than 2): "))
        if num_floors < 2:
            print("Invalid input. The elevator's capacity should be at least one person")
        else:
            break

    # Initialize a list to store the queues for each floor
    floor_queues = []
    # Iterate through each floor to determine if there are people waiting
    for i in range(num_floors):
        floor_i_passengers = []
        # Check if user wants to add people waiting on this floor
        while True:
            # Ask the user if there are people waiting on the current floor
            add_or_not = input(f"Are there any people waiting for the elevator on floor {i}? (y for yes / n for no): ")
            if add_or_not not in ("y", "n"):
                print("Incorrect input, please only type 'y' or 'n'")
            else:
                break
        if add_or_not == "y":
            count = 0
            while True:
                count += 1
                # Add the destination floor of the person waiting on the current floor
                floor_i_passengers.append(int(input(f"for floor {i}, please input person {count} destination: ")))
                # Ask the user if they want to add more people's destinations on this floor
                while True:
                    continue_or_not = input("Do you want do add more people's destinations on this floor? (y for yes / n for no): ")
                    if continue_or_not not in ("y", "n"):
                        print("Incorrect input, please only type 'y' or 'n'")
                    else:
                        break
                if continue_or_not == "n":
                    break
        # Add the list of people waiting on the current floor to the floor_queues list
        floor_queues.append(floor_i_passengers)

    # Initialize an elevator object with the parameters given by the user
    elevator = Elevator(num_floors, elevator_capacity, floor_queues)
    # Run the elevator simulation
    elevator.run_elevator()
    print("Elevator simulation completed.")

    # Example parameters:
    # num_floors = 5
    # elevator_capacity = 3

    # Example queue:
    # First line is for floor 0, Second for floor 1 etc
    # Priority in each floor's queue goes from left to right
    # floor_queues = [
    #     [2, 3, 4],
    #     [],
    #     [1, 3],
    #     [4],
    #     []
    # ]

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
