import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

# 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if graph[x][y] == 1:
        return False

    stack = [(x, y)]
    graph[x][y] = 1  # 방문 표시

    while stack:
        cx, cy = stack.pop()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            # 범위 및 방문 검사
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                stack.append((nx, ny))

    return True

result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1  # 묶음 개수

print(result)
