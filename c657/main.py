# Input
def parse(s: str) -> list[str]: 
    return s.strip().splitlines()

from itertools import groupby
# Process
def longest_count(s: str) -> str: 
    g = map(lambda t: (t[0], len(list(t[1]))), groupby(s))
    freq = sorted(g, key=lambda x: (x[1]), reverse=True)
    
    return "%s %d" % freq[0]

# Output
def main(args): 
    result = map(longest_count, parse(args))
    return "\n".join(result)

# Entry Point
if __name__ == "__main__":
    import sys
    args = sys.stdin.read()
    print(main(args))
