# Input
def parse(s: str) -> list[int]: 
    return map(int, s.strip().splitlines()) # type: ignore

# Process
def permute(n: int) -> str:
    seed = list(range(1, n+1))
    
    def p(l:list[int]) -> list[list[int]]:
        if len(l) == 1: return [l]
        return [[i] + j for i in l for j in p([k for k in l if k != i])]
    
    result = sorted(list(map(lambda l: "".join(map(str, l)), p(seed))), reverse=True)
    return "\n".join(map(str,result))

# Output
def main(args): 
    result = map(permute, parse(args))
    return "\n".join(result)

# Entry Point
if __name__ == "__main__":
    import sys
    args = sys.stdin.read()
    print(main(args))
