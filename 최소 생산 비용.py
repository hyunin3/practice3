def dfs(n, sm):
    global ans
    if ans <= sm:
        return

    if n == N:
        if ans > sm:
            ans = sm
        return

    for i in range(N):
        if v[i] == 0:
            v[i] = 1
            dfs(n+1, sm + arr[n][i])
            v[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * N
    ans = 1000000
    dfs(0, 0)
    print(f'#{tc} {ans}')