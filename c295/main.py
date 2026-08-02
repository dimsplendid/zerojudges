# standard IPO template

# Input

from typing import Iterable
 
def parse(s: str) -> Iterable[Iterable[int]]: 
    _, *groups = s.splitlines() # skip 0-th line
    return map(lambda g: map(int, str.split(g)), groups)

# Process
# def max(group: list[int]) -> int: 
#     ...

# Output
def main(args): 
    result = list(map(max, parse(args)))
    summary = sum(result)
    divisible = ' '.join(map(str,filter(lambda x: summary % x == 0, result)))
    if divisible == '': divisible = '-1'
    return "\n".join([str(summary), divisible])

# Entry Point
if __name__ == "__main__":
    import sys
    args = sys.stdin.read()
    print(main(args))
