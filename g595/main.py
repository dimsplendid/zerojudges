# standard IPO template

# Input
def parse(s: str) -> list[tuple[int, int]]: 
    # 3 0 2 0 1 -> [3, 2], [2, 1]
    _, hs = s.splitlines()
    hs = [100] + list(map(int, hs.split())) + [100]
    parsed = [(hs[i-1], hs[i+1]) for i, h in enumerate(hs) if h == 0]
    return parsed

# Process
# def min_(hs: tuple[int, int]) -> int: 
#     ...

# Output
def main(args): 
    result = sum(map(min, parse(args)))
    return result

# Entry Point
if __name__ == "__main__":
    import sys
    args = sys.stdin.read()
    print(main(args))
