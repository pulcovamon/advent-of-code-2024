from copy import copy


class Direction:
    UP = "up"
    DOWN = "down"
    RIGHT = "right"
    LEFT = "left"


class GuardWalk:
    def __init__(self, lab_map):
        self.map = [line.strip() for line in lab_map]
        self.direction = Direction.UP
        self.visited = set()
        self.is_in_map = True
        self.find_start_position()
        self.loops = 0

    def find_start_position(self):
        for i in range(len(lines)):
            x_candidate = self.map[i].find("^")
            if x_candidate != -1:
                self.x = x_candidate
                self.y = i
                self.start_x = self.x
                self.start_y = self.y
                self.visited.add((self.x, self.y))
                break

    def go_up(self):
        if self.y > 0:
            if self.map[self.y - 1][self.x] != "#":
                self.y -= 1
            else:
                self.direction = Direction.RIGHT
                self.go_right()
        else:
            self.is_in_map = False

    def go_right(self):
        if self.x < len(self.map[self.y]) - 1:
            if self.map[self.y][self.x + 1] != "#":
                self.x += 1
            else:
                self.direction = Direction.DOWN
                self.go_down()
        else:
            self.is_in_map = False

    def go_down(self):
        if self.y < len(self.map[self.y]) - 1:
            if self.map[self.y + 1][self.x] != "#":
                self.y += 1
            else:
                self.direction = Direction.LEFT
                self.go_left()
        else:
            self.is_in_map = False

    def go_left(self):
        if self.x > 0:
            if self.map[self.y][self.x - 1] != "#":
                self.x -= 1
            else:
                self.direction = Direction.UP
                self.go_up()
        else:
            self.is_in_map = False

    def step(self):
        match self.direction:
            case Direction.UP:
                self.go_up()
            case Direction.RIGHT:
                self.go_right()
            case Direction.DOWN:
                self.go_down()
            case Direction.LEFT:
                self.go_left()
            case _:
                raise ValueError(f"{self.x}, {self.y}, {self.direction}")

    def walk(self):
        while self.is_in_map:
            self.step()
            self.visited.add((self.x, self.y))
        return len(self.visited)

    def creates_loop(self, x, y):
        currently_visited = {(self.x, self.y)}
        current_path = [(self.x, self.y)]
        previous = (self.x, self.y)
        while self.is_in_map:
            self.step()
            current = (self.x, self.y)
            if {current, previous}.issubset(currently_visited):
                if [
                    i
                    for i in range(1, len(current_path))
                    if current_path[i - 1] == previous and current_path[i] == current
                ]:
                    return True
            current_path.append(current)
            currently_visited.add(current)
            previous = current
        return False

    def find_positions_for_loop(self):
        self.visited.remove((self.start_x, self.start_y))
        count = 0
        for x, y in list(self.visited):
            self.is_in_map = True
            self.direction = Direction.UP
            self.x = self.start_x
            self.y = self.start_y
            original_map = copy(self.map)
            self.map[y] = f"{self.map[y][:x]}#{self.map[y][x+1:]}"
            if self.creates_loop(x, y):
                count += 1
            self.map = original_map
        return count


if __name__ == "__main__":
    with open("06.txt", "r") as input_file:
        lines = input_file.readlines()

    guard_walk = GuardWalk(lines)
    result = guard_walk.walk()
    print(f"Number of visited places: {result}")

    result = guard_walk.find_positions_for_loop()
    print(f"Number of candidates for an obstacle: {result}")
