# Input
def parse(s: str) -> list[tuple[int, int]]: 
    _, *lines = s.strip().splitlines()
    return map(lambda l: map(int, l.strip().split()), lines)

from enum import Enum

class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

# Process
def helix_mat(n: int, c: int) -> str:
    """
    n: n dimensions sqare matrix
    c: rotation option, 1 -> clockwise, 2 -> counter clockwise
    """
    m = [[0 for _ in range(n)] for _ in range(n)]

    if c == 1:
        d = Direction.RIGHT
        x, y = 0, 0
        for i in range(1, n*n+1):
            m[y][x] = i
            dx, dy = d.value
            if x+dx == n or x+dx == -1 or y+dy == n or y+dy == -1 or m[y+dy][x+dx] != 0: # hit wall
                match d:
                    case Direction.RIGHT: d = Direction.DOWN
                    case Direction.DOWN:  d = Direction.LEFT
                    case Direction.LEFT:  d = Direction.UP
                    case Direction.UP:    d = Direction.RIGHT
                dx, dy = d.value
            x += dx
            y += dy
            
    if c == 2:
        d = Direction.DOWN
        x, y = 0, 0
        for i in range(1, n*n+1):
            m[y][x] = i
            dx, dy = d.value
            if x+dx == n or x+dx == -1 or y+dy == n or y+dy == -1 or m[y+dy][x+dx] != 0: # hit wall
                match d:
                    case Direction.RIGHT: d = Direction.UP
                    case Direction.DOWN:  d = Direction.RIGHT
                    case Direction.LEFT:  d = Direction.DOWN
                    case Direction.UP:    d = Direction.LEFT
                dx, dy = d.value
            x += dx
            y += dy

    return "\n".join(map(lambda r: "".join(map(lambda n: f"{n:>5}", r)), m))

# Output
def main(args): 
    result = map(lambda x: helix_mat(*x), parse(args))
    return "\n".join(result)

# Entry Point
if __name__ == "__main__":
    import sys
    args = sys.stdin.read()
    print(main(args))
