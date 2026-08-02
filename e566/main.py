# Input
def parse(s: str) -> list[tuple[int]]: 
    lines = s.strip().splitlines()
    return map(lambda l: map(int, l.strip().split()), lines)

# Process
def power_seq(n: int, m: int) -> str:
    if m == 0: return "Boring!"
    def f(n, m):
        if n == 1: return [1]
        if n >= m and n % m == 0:
            return [n] + f(n//m, m)
        return [None]
    result = f(n, m)
    return " ".join(map(str, result)) if result[-1] is not None else "Boring!"

# Output
def main(args): 
    result = map(lambda x: power_seq(*x), parse(args))
    return "\n".join(result)

# Entry Point
if __name__ == "__main__":
    import sys
    args = sys.stdin.read()
    print(main(args))
