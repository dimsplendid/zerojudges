import sys

def parser(s):
    s.split() # s.splitlines().split() # 視測資格式選合適的
    ...

def solution(x):
    ...

if __name__ == "__main__":
    s = sys.stdin.read().split() # sys.stdin.readlines() # 視測資格式選合適的
    results = map(solution, s)
    print("\n".join(results))