# Input
def parse(s: str) -> list[str]: 
    return list(s.strip())

# Process
def decode(s: list[str]) -> str: 
    result = [ abs(ord(s[i])-ord(s[i+1])) for i in range(6) ]
    return "".join(map(str, result))
    
# Output
def main(args): 
    result = decode(parse(args))
    return result

# Entry Point
if __name__ == "__main__":
    import sys
    args = sys.stdin.read()
    print(main(args))
