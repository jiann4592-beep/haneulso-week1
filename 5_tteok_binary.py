import sys
input = sys.stdin.readline

n, m = map(int, input().split())
heights = list(map(int, input().split()))

# 탐색 범위
start, end = 0, max(heights)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0

    # 잘린 길이
    for h in heights:
        if h > mid:
            total += h - mid

    if total < m:
        end = mid - 1  # 높이 낮추기
    else:
        result = mid  # 가능한 높이
        start = mid + 1  # 높이 높이기

print(result)
