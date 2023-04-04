def dfs(s):
    # 방문표시: 첫 방문시 처리할 일 있으면 이곳에서..!
    v[s] = 1
    alst.append(s)
 
    for e in adj[s]:
        if v[e]==0:     # 연결된 노드이고 미방문시
            dfs(e)
 
T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)    # 양방향 연결이므로..
 
    # 여러개 연결시 낮은번호부터 방문! => 오름차순 정렬!!!
    for i in range(1, V+1):
        adj[i].sort()
 
    v = [0]*(V+1)
    alst = []
    dfs(1)
 
    print(f'#{test_case}', *alst)