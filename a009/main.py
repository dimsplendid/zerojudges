# standard IPO template

# Input
# def parse(s: str) -> str: 
#     ...

# Process
def decode(s:str) -> str: 
    return "".join(map(lambda c: chr(c-7), map(ord, s)))

# Output
def main(args): 
    return decode(args)

# Entry Point
if __name__ == "__main__":
    import sys
    args = sys.stdin.read()
    print(main(args))
