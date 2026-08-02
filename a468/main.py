# Input
month = {
    "January"  :1,
    "February" :2,
    "March"    :3,
    "April"    :4,
    "May"      :5,
    "June"     :6,
    "July"     :7,
    "August"   :8,
    "September":9,
    "October"  :10,
    "November" :11,
    "December" :12,
}

def parse(s: str) -> list[tuple[tuple[int, int, int], tuple[int, int, int]]]: 
    n, *lines = s.strip().splitlines()
    def parse_date(d):
        m, d, y = d.split()
        return int(y), month[m], int(d[:-1])
    lines = list(map(parse_date,lines))
    return [(i+1, lines[2*i], lines[2*i+1]) for i in range(int(n))]

# Process
def leap_count(case: int, date1: tuple[int, int, int], date2: tuple[int, int, int]) -> str:
    def leap_count_up(y: int):
        return y // 400 + y // 4 - y // 100 # 排容原理
    # print(date1, date2)
    # start year: if over 2/28, start with next year
    start = date1[0] if date1[1] < 2 or (date1[1] == 2 and date1[2] <= 29) else date1[0] + 1
    # end year: if before 2/28, end with previous year
    end = date2[0] if date2[1] > 2 or (date2[1] == 2 and date2[2] == 29) else date2[0] - 1  
    # print(case, start, end)
    return f"Case {case}: {leap_count_up(end) - leap_count_up(start-1)}"
        

# Output
def main(args): 
    result = map(lambda x: leap_count(*x), parse(args))
    return "\n".join(result)

# Entry Point
if __name__ == "__main__":
    import sys
    args = sys.stdin.read()
    print(main(args))
