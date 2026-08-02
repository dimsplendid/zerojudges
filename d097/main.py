# Input
def parse(s: str) -> list[list[int]]: 
    def parse_line(xs):
        _, *nums = xs.split() # neglect first number
        return list(map(int, nums))
    return map(parse_line, s.splitlines())

# Process
def check_jolly(l: list[int]) -> str: 
    diff = [abs(l[i+1] - l[i]) for i in range(len(l)-1)]
    judge = sorted(diff) == list(range(1, len(l)))
    return "Jolly" if judge else "Not jolly"

# Output
def main(args): 
    result = map(check_jolly, parse(args))
    return "\n".join(result)

# Entry Point
if __name__ == "__main__":
    import sys
    args = sys.stdin.read()
    print(main(args))
