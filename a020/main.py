# standard IPO template

# Input
# def parse(s: str) -> str:
#     ...

alphabet_dict = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    'G': 16,
    'H': 17,
    'I': 34,
    'J': 18,
    'K': 19,
    'L': 20,
    'M': 21,
    'N': 22,
    'O': 35,
    'P': 23,
    'Q': 24,
    'R': 25,
    'S': 26,
    'T': 27,
    'U': 28,
    'V': 29,
    'W': 32,
    'X': 30,
    'Y': 31,
    'Z': 33,
}

# Process
def verify(s: str) -> str: 
    a, *ns = list(s)
    a = alphabet_dict[a]
    ns = list(map(int, ns[0:9]))
    # print(a, ns)
    verify_nums = sum([
        a % 10 * 9 + a // 10,
        sum([ns[7-i] * (i+1) for i in range(8)]),
        ns[8],
    ])
    # print(verify_nums)
    if verify_nums % 10 == 0: return 'real'
    return 'fake'

# Output
def main(args): 
    result = verify(args)
    return result

# Entry Point
if __name__ == "__main__":
    import sys
    args = sys.stdin.read()
    print(main(args))
