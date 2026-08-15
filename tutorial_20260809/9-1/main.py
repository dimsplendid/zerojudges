# Input
def parse(s: str) -> list[tuple[str, str]]: # type hint
    lines = s.splitlines()
    def parse_line(s: str) -> tuple[str, str]:
        return tuple(s.split())
    return list(map(parse_line, lines))

# Process
def weather_info(temperature:str, weather:str) -> str:
    return f"今天的氣溫是 {temperature} 度, 天氣是 {weather} 天"

# Output
def output(out: list[str]):
    print("\n".join(out))

if __name__ == "__main__":
    import sys
    # output(map(lambda s: weather_info(*s), parse(sys.stdin.read())))
    result = []
    for t, w  in parse(sys.stdin.read()):
        result.append(weather_info(t,w))
    output(result)
