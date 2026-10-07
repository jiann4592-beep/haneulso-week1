import sys
input = sys.stdin.readline

n, m = map(int, input().split())
heights = list(map(int, input().split()))

start, end = 0, max(heights)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    for h in heights:
        if h > mid:
            total += h - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)