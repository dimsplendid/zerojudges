# Input
def parse(s: str) -> list[int]: 
    return list(map(int, list(s.strip())))

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
def candidate(ns: list[int]) -> str: 
    verify_nums = sum([ns[7-i] * (i+1) for i in range(8)]) + ns[8]
    # print(alphabet_dict.items())
    result = map(lambda kv: kv[0], filter(lambda kv: (kv[1] * 9 + kv[1] // 10 + verify_nums) % 10 == 0, alphabet_dict.items()))
    return "".join(result)

# Output
def main(args): 
    result = candidate(parse(args))
    return result

# Entry Point
if __name__ == "__main__":
    import sys
    args = sys.stdin.read()
    print(main(args))
