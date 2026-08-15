def parse(s: str) -> list[tuple[int, int, int, list[int]]]:
    lines = s.splitlines()
    def parse_line(line1: str, line2: str) -> tuple[int, int, int, list[int]]:
        v, w, r = line1.split()
        _, *house_dists = line2.split()
        return int(v), int(w), int(r), list(map(int,house_dists))
    result = [parse_line(lines[2*i], lines[2*i+1]) for i in range(len(lines)//2)]
    return result

def is_safe(
    villager: int,
    wolfman: int,
    attack_range: int,
    house_dists: list[int],
) -> str:
    begin, end = (villager, wolfman) if wolfman > villager else (wolfman, villager)
    vw_dist = sum(house_dists[begin:end])
    return "Yes" if vw_dist < attack_range else "No"
    

def output(s: list[str]):
    print("\n".join(s))

if __name__ == "__main__":
    import sys
    s = sys.stdin.read()
    # print(parse(s))
    output(map(lambda x: is_safe(*x), parse(s)))
