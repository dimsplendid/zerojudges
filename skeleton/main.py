# Input
def parse(s: str) -> list[tuple[... ] ]: 
    # _, *lines = s.strip().splitlines()
    ...

# Process
def SOLUTION(*args: tuple[...] ) -> str: 
    ...

# Output
def output(args): 
    result = map(lambda x: SOLUTION(*x), parse(args))
    return "\n".join(result)

# Entry Point
if __name__ == "__main__":
    import sys
    args = sys.stdin.read()
    print(output(args))
