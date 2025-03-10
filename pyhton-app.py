def result(inputfile):
    map = []
    moves = ""
    readingMap = True
    with open(inputfile) as f:
        for line in f:
            if readingMap:
                if len(line) == 1:
                    readingMap = False
                    continue
                tiles = [*line.strip()]
                map.append(tiles)
            else:
                moves += line.strip()

    for i, row in enumerate(map):
        for j, value in enumerate(row):
            if value == "@":
                y_robot = i
                x_robot = j

    def move(direction, x, y):
        match direction:
            case "v":
                next_x = x
                next_y = y + 1
                nextTile = map[next_y][next_x]
            case "^":
                next_x = x
                next_y = y - 1
                nextTile = map[next_y][next_x]
            case ">":
                next_x = x + 1
                next_y = y
                nextTile = map[next_y][next_x]
            case "<":
                next_x = x - 1
                next_y = y
                nextTile = map[next_y][next_x]

        if nextTile == "#":
            return False
        elif nextTile == ".":
            map[next_y][next_x] = map[y][x]
            map[y][x] = "."
        else:
            move_possible = move(direction, next_x, next_y)
            if not move_possible:
                return False
            else:
                map[next_y][next_x] = map[y][x]
                map[y][x] = "."

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

    result = 0
    for i, row in enumerate(map):
        for j, value in enumerate(row):
            if value == "O":
                result += 100 * i + j

    return result


print(result("input.txt"))
