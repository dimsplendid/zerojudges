# standard IPO template

# Input
def parse(s: str) -> list[list[int]]: 
    _, *lines= s.splitlines() # skip 0-th line
    return map(lambda xs: list(map(int, xs.split())), lines)

# Process
from enum import Enum

class Seq(Enum):
    AS = "AS"
    GS = "GS"

def predict(l: list[int]) -> str: 
    def check_ratio(l: list[int]) -> tuple[Seq, int]:
        if l[1] - l[0] == l[2] - l[1]:
            return Seq.AS, l[1] - l[0]
        return Seq.GS, l[1] // l[0]
    seq_type, d = check_ratio(l)
    match seq_type:
        case Seq.AS: result = l + [l[-1] + d]
        case Seq.GS: result = l + [l[-1] * d]
    return " ".join(map(str, result))
# Output
def main(args): 
    result = map(predict, parse(args))
    return "\n".join(result)

# Entry Point
if __name__ == "__main__":
    import sys
    args = sys.stdin.read()
    print(main(args))
