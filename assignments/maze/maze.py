# 공식 제출용 - 김민찬 2023059889

if __name__ == "__main__":

    maze = []
    maze_col = 0
    maze_row = 0

    # Read maze
    while True:
        try:
            line = input().strip()
            if not line:
                break
            
            tiles = list(line)
            if maze_col == 0:
                maze_col = len(tiles)
            maze_row += 1

            maze.append(tiles)

        except EOFError:
            break
    
    # find starting point - DFS
    pos_x, pos_y = 0, 0

    for x in range(1, maze_col):
        #print(f"cell is {maze[pos_y][x]}")
        if maze[pos_y][x] == 'A':
            # print("starting pos found!")
            pos_x = x
            break
        
    # print(f"starting pos = {pos_y}, {pos_x}")

    # start scan
    path = 1
    pos_y = 1

    while maze[pos_y][pos_x] != "B":
        pos = maze[pos_y][pos_x]

        # for debug
        if pos == "1":
            print(f"invalid tile. current position {maze[pos_y][pos_x]}")
            break

        # scan down - right - left - up in order, count moves

        # scan down
        if maze[pos_y + 1][pos_x] == "0" or maze[pos_y + 1][pos_x] == "B":
            maze[pos_y][pos_x] = "#"
            pos_y += 1
            path += 1
            continue
        # scan right
        elif maze[pos_y][pos_x + 1] == "0" or maze[pos_y][pos_x + 1] == "B":
            maze[pos_y][pos_x] = "#"
            pos_x += 1
            path += 1
            continue
        # scan left
        elif maze[pos_y][pos_x - 1] == "0" or maze[pos_y][pos_x - 1] == "B":
            maze[pos_y][pos_x] = "#"
            pos_x -= 1
            path += 1
            continue
        # scan up
        elif maze[pos_y - 1][pos_x] == "0"  or maze[pos_y - 1][pos_x] == "B":
            maze[pos_y][pos_x] = "#"
            pos_y -= 1
            path += 1
            continue
        # no direction, backtrack
        else:
            # scan up
            if maze[pos_y - 1][pos_x] == "#":
                maze[pos_y][pos_x] = "1"
                pos_y -= 1
                path -= 1
                continue
            # scan right
            elif maze[pos_y][pos_x + 1] == "#":
                maze[pos_y][pos_x] = "1"
                pos_x += 1
                path -= 1
                continue
            # scan left
            elif maze[pos_y][pos_x - 1] == "#":
                maze[pos_y][pos_x] = "1"
                pos_x -= 1
                path -= 1
                continue
            # scan down
            elif maze[pos_y + 1][pos_x] == "#":
                maze[pos_y][pos_x] = "1"
                pos_y += 1
                path -= 1
                continue

    # print path
    print(path)

