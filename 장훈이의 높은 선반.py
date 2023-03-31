def dfs(n, sm):
    global ans
    if n == N:
        if sm >= B:
            ans = min(ans, B - sm)
        return
       
    dfs(n+1, sm+lst[n])
    dfs(n+1, sm)    

T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    dfs(0, 0)
    ans = 0
    print(f'#{tc} {ans}')