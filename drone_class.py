import random

class Drone:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = self.set_direction()
        self.active = False
    
    def set_direction(self):
        x = self.x
        y = self.y
        if x == 0:
            if y == 0:
                direction = random.choice([1, 2])
            elif y == 9:
                direction = random.choice([1, 3])
            else:
                direction = random.choice([1, 2, 3])
        elif x == 9:
            if y == 0:
                direction = random.choice([0, 2])
            elif y == 9:
                direction = random.choice([0, 3])
            else:
                direction = random.choice([0, 2, 3])
        else:
            direction = random.choice([0, 1, 2, 3])
        self.direction = direction
    
    def move(self, grid_size):
        direction = self.direction
        if self.active:
            new_x, new_y = self.x, self.y
            if direction == 0 and self.y < grid_size - 1:
                new_y += 1
            elif direction == 1 and self.y > 0:
                new_y -= 1
            elif direction == 2 and self.x < grid_size - 1:
                new_x += 1
            elif direction == 3 and self.x > 0:
                new_x -= 1
            if 0 <= new_x < grid_size and 0 <= new_y < grid_size:
                self.x, self.y = new_x, new_y

    def make_active(self):
        self.active = True