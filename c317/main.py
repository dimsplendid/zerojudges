# Input
def parse(s: str) -> list[tuple[int, int, int]]: 
    _, *lines = s.strip().splitlines()
    return map(lambda l: map(int, l.strip().split()), lines)

# Process
def match_coins(total: int, a: int, b: int) -> str:
    # total = a * x + b * y
    # x + y minimum
    for y in range(total // b + 1):
        res = total - b * y
        if res % a == 0:
            return str(res // a + y)
    return str(-1)

# Output
def main(args): 
    result = map(lambda x: match_coins(*x), parse(args))
    return "\n".join(result)

# Entry Point
if __name__ == "__main__":
    import sys
    args = sys.stdin.read()
    print(main(args))
