from collections import deque

def bfs(maze, visited, sy, sx, dead, goal):
    queue = deque([[sy, sx]])
    visited[sy][sx] = 0
    count = 0
    while queue:
        y, x = queue.popleft()
        print(maze[y][x], goal)
        if maze[y][x] == goal:
            count += 1
        for j, k in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            new_y, new_x = y+j, x+k
            if not maze[new_y][new_x] in dead and \
                visited[new_y][new_x] == -1:
                visited[new_y][new_x] = visited[y][x] + 1
                queue.append([new_y, new_x])
    return count % 1000000007
if __name__ == "__main__":
    n,m=map(int, input().split())
    a=[int(input()) for i in range(m)]
    maze=[[2*i+j for i in range(int(n/2+1))] for j in range(n+1)]
    visited = [[[-1] for i in range(int(n/2+1))] for j in range(n+1)]
    print(bfs(maze, visited, 0, 0, a, n))
