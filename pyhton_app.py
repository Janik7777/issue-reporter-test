"""
solve exercise
"""


def result(inputfile):
    """
    compute result of exercise
    """
    my_map = []
    moves = ""
    reading_map = True
    with open(inputfile, encoding="utf-8") as f:
        for line in f:
            if reading_map:
                if len(line) == 1:
                    reading_map = False
                    continue
                tiles = [*line.strip()]
                my_map.append(tiles)
            else:
                moves += line.strip()

    for i, row in enumerate(my_map):
        for j, value in enumerate(row):
            if value == "@":
                y_robot = i
                x_robot = j

    def move(direction, x, y):
        """
        make a move in the direction
        """
        match direction:
            case "v":
                next_x = x
                next_y = y + 1
                next_tile = my_map[next_y][next_x]
            case "^":
                next_x = x
                next_y = y - 1
                next_tile = my_map[next_y][next_x]
            case ">":
                next_x = x + 1
                next_y = y
                next_tile = my_map[next_y][next_x]
            case "<":
                next_x = x - 1
                next_y = y
                next_tile = my_map[next_y][next_x]

        if next_tile == "#":
            return False
        elif next_tile == ".":
            my_map[next_y][next_x] = my_map[y][x]
            my_map[y][x] = "."
        else:
            move_possible = move(direction, next_x, next_y)
            if not move_possible:
                return False
            else:
                my_map[next_y][next_x] = my_map[y][x]
                my_map[y][x] = "."

        return True

    for direction in moves:
        if move(direction, x_robot, y_robot):
            match direction:
                case "v":
                    y_robot += 1
                case "^":
                    y_robot -= 1
                case ">":
                    x_robot += 1
                case "<":
                    x_robot -= 1

    result_of_function = 0
    for i, row in enumerate(my_map):
        for j, value in enumerate(row):
            if value == "O":
                result_of_function += 100 * i + j

    return result_of_function


print(result("input.txt"))
