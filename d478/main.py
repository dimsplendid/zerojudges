# Input
def parse(s: str) -> list[tuple[list[int], list[int]]]: 
    _, *lines = s.strip().splitlines() # skip 0th line
    lines = list(map(lambda l: list(map(int, l.strip().split())), lines))
    return [(lines[2*i], lines[2*i+1]) for i in range(len(lines)//2)]

# Process
def common_number(a: list[int], b: list[int]) -> str: 
    return str(len(set(a) & set(b)))

# Output
def main(args): 
    result = map(lambda x: common_number(*x), parse(args))
    return "\n".join(result)

# Entry Point
if __name__ == "__main__":
    import sys
    args = sys.stdin.read()
    print(main(args))
