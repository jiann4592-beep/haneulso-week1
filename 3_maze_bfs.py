from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

distance = [[0] * m for _ in range(n)]


def bfs():
    queue = deque([(0, 0)])
    distance[0][0] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if distance[nx][ny] != 0:
                continue

            distance[nx][ny] = distance[x][y] + 1
            queue.append((nx, ny))

    return distance[n - 1][m - 1]


print(bfs())
