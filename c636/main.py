# standard IPO template

# Input
def parse(s: str) -> list[int]:
    return map(int, s.splitlines())

# Process
def zodiac(y: int) -> str: 
    z = ['鼠', '牛', '虎', '兔', '龍', '蛇', '馬', '羊', '猴', '雞', '狗', '豬']
    y = y + 1911
    return z[(y-4) % 12]

# Output
def main(args): 
    result = map(zodiac, parse(args))
    return "\n".join(result)

# Entry Point
if __name__ == "__main__":
    import sys
    args = sys.stdin.read()
    print(main(args))
