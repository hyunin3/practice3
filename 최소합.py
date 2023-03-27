def dfs(i, j, sm):
    global ans

    if sm >= ans:
        return

    if i == N-1 and j == N-1:  #종료조건
        if sm < ans:
            ans = sm
        return

    for di, dj in ((0,1), (1,0)):
        ni, nj = i + di, j + dj

        if 0 <= ni < N and 0 <= nj < N:
            dfs(ni, nj, sm + arr[ni][nj])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 1000000
    dfs(0, 0, arr[0][0]) #첫 줄 제일 왼쪽 칸에서 시작

    print(f'#{tc} {ans}')
