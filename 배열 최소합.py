def dfs(n, sm):
    global ans
    #가지치기는 가장 위, 가장 나중에 추가
    if ans <= sm:
        return
    
    if n == N: # 종료조건(n관련). 반드시 이 곳에서만
        if sm < ans: # 최솟값 갱신
            ans = sm
        return

    #하부호출(정해지지 않은 개수인 경우 for문)
    for i in range(N):
        if v[i] == 0:
            v[i] = 1
            dfs(n+1, sm + arr[n][i])
            v[i] = 0
        
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 1000000
    v = [0]*N
    dfs(0, 0)
    
    print(f'#{tc} {ans}')