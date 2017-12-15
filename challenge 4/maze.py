movements = {'north': (-1, 0), 'east': (0, 1), 'south': (1, 0), 'west': (0, -1)}


class Position:
    def __init__(self, coords, moves):
        self.coords = coords
        self.moves = moves
        self.wall_demolished = False
        self.previous_positions = []


def answer(maze):
    end = (len(maze) - 1, len(maze[len(maze) - 1]) - 1)
    starting_position = Position((0, 0), 1)
    queue = [starting_position]
    while len(queue) > 0:
        current_position = queue.pop(0)
        current_position.previous_positions.append(current_position.coords)
        for movement in movements:
            new_coordinates = (current_position.coords[0] + movements[movement][0], current_position.coords[1] + movements[movement][1])
            new_position = Position(new_coordinates, current_position.moves + 1)
            new_position.wall_demolished = current_position.wall_demolished
            if new_position.coords == end:
                return new_position.moves
            if not 0 <= new_position.coords[0] <= end[0] or not 0 <= new_position.coords[1] <= end[1]:
                # out of bounds
                continue
            if new_position.coords in current_position.previous_positions:
                # already checked
                continue
            if maze[new_position.coords[0]][new_position.coords[1]] == 1:
                # wall
                if new_position.wall_demolished:
                    # can't demolish another, can't go that way
                    continue
                else:
                    new_position.wall_demolished = True

            # add to appropriate queue
            new_position.previous_positions = list(current_position.previous_positions)
            if movement in ['east', 'south']:
                queue.insert(0, new_position)
            else:
                queue.append(new_position)
    return 0


# test_maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1], [0, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
test_maze = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0], [0, 1, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0]]
print(answer(test_maze))
