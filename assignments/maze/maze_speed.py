# 공식 제출 아님 - 속도/최적화 실험 코드
import sys
sys.setrecursionlimit(10**7)

if __name__ == "__main__":
    data = sys.stdin.read().splitlines()
    if not data:
        sys.exit(0)

    H = len(data)
    W = len(data[0].rstrip())
    total = H * W

    # Build a single 1D array “grid” of length H*W:
    #   1 => wall (or “visited”)
    #   0 => open path
    # We also record “start” (just below 'A') and “end” (index of 'B').
    grid = [0] * total
    start = end = None

    for y, raw in enumerate(data):
        row = raw.rstrip()
        base = y * W
        for x, c in enumerate(row):
            idx = base + x
            if c == '1':
                grid[idx] = 1
            else:
                grid[idx] = 0
                if y == 0 and c == 'A':
                    # start one row down
                    start = (1 * W) + x
                elif c == 'B':
                    end = idx

    # If no A or no B, quit
    if start is None or end is None:
        print(-1)
        sys.exit(0)

    # Mark the “cell above start” as visited, so we don't climb back onto row 0
    above_start = start - W
    if above_start >= 0:
        grid[above_start] = 1
    # Mark start itself as visited too
    grid[start] = 1

    # We'll do an explicit DFS with our own stack of tuples:
    #   (pos, next_dir_to_try, path_length)
    #
    # next_dir_to_try ∈ {0,1,2,3,4}
    #   0 => we haven't tried “down” yet
    #   1 => we need to try “right” next
    #   2 => we need to try “left”
    #   3 => we need to try “up”
    #   4 => all 4 directions done → pop/backtrack
    #
    # Path length starts at 1 (first step dropped into row 1).
    stack = [(start, 0, 1)]  # (index, dir_idx, path_len)

    while stack:
        pos, dir_idx, length = stack[-1]

        # If we reached the goal cell, print and exit
        if pos == end:
            print(length)
            break

        # Otherwise, try the next direction
        if dir_idx == 0:
            # down  => pos + W
            stack[-1] = (pos, 1, length)
            new = pos + W
            if new < total and grid[new] == 0:
                grid[new] = 1
                stack.append((new, 0, length + 1))
                continue

        elif dir_idx == 1:
            # right => pos + 1  (only if not at right‐edge)
            stack[-1] = (pos, 2, length)
            if (pos % W) < (W - 1):
                new = pos + 1
                if grid[new] == 0:
                    grid[new] = 1
                    stack.append((new, 0, length + 1))
                    continue

        elif dir_idx == 2:
            # left  => pos - 1  (only if not at left‐edge)
            stack[-1] = (pos, 3, length)
            if (pos % W) > 0:
                new = pos - 1
                if grid[new] == 0:
                    grid[new] = 1
                    stack.append((new, 0, length + 1))
                    continue

        elif dir_idx == 3:
            # up    => pos - W
            stack[-1] = (pos, 4, length)
            new = pos - W
            if new >= 0 and grid[new] == 0:
                grid[new] = 1
                stack.append((new, 0, length + 1))
                continue

        else:
            # dir_idx == 4 → all directions exhausted → backtrack
            stack.pop()
            continue

    else:
        # If we emptied the stack without finding 'B', no path exists
        print(-1)
