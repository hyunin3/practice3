def dfs(v):
    visited[v] = 1
 
    for nxt in graph[v]:
        if visited[nxt]:
            continue
        dfs(nxt)
 
T = int(input())
for tc in range(1, 1 + T):
    N, M = map(int, input().split())
    tmp = list(map(int, input().split()))
    graph = [[] for _ in range(N + 1)]
 
    for i in range(M):
        v1 = tmp[i * 2]
        v2 = tmp[i * 2 + 1]
        graph[v1].append(v2)
        graph[v2].append(v1)
 
    visited = [0] * (N+1)
    cnt = 0
 
    for i in range(1, N + 1):
        if visited[i]:
            continue
        dfs(i)
        cnt += 1
    print(f'#{tc} {cnt}')