# standard IPO template

# Input
def parse(s: str) -> list[int]: # [a, b], a > b
    return sorted(list(map(int, s.split())), reverse=True)

# Process
def gcd(xs: list[int]) -> int: 
    a, b = xs
    r = a % b
    if r == 0: return b
    else: return gcd([b, r])

# Output
def main(args): 
    result = gcd(parse(args))
    return result

# Entry Point
if __name__ == "__main__":
    import sys
    args = sys.stdin.read()
    print(main(args))
