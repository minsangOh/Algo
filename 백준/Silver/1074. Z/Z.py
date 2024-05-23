n, r, c = map(int, input().split())
def ZZZ(n, r, c):
    if n == 0: return 0
    n = 2 * (r % 2) + (c % 2) + 4 * ZZZ(n - 1, r // 2, c // 2)
    return n
print(ZZZ(n, r, c))