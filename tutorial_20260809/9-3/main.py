noise = "()-[]{};:<>?@#$%^&*"
# Input
def parse(s: str) -> list[str]:
    line = s.splitlines()
    return line
# Process
def decode(s: str) -> str:
    def check_symbol(c):
        if c in noise: return False
        return True
    return "".join(filter(check_symbol, s))
    
# Output
def output(s: list[str]):
    print("\n".join(s))

if __name__ == "__main__":
    import sys
    s = sys.stdin.read()
    output(map(decode, parse(s)))
