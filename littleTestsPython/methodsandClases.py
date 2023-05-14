class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current

    def up(self):
        """Makes the elevator go up one floor."""
        if self.current < self.top:
            self.current += 1

    def down(self):
        """Makes the elevator go down one floor."""
        if self.current > self.bottom:
            self.current -= 1

    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        if self.bottom <= floor <= self.top:
            self.current = floor


elevator = Elevator(-1, 10, 0)

elevator.up() 
print(elevator.current) #should output 1

elevator.down() 
print(elevator.current) #should output 0

elevator.go_to(10) 
print(elevator.current) #should output 10