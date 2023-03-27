def dfs(n, cnt, sm):
    global ans
    
    # if cnt > CNT or sm > K:
    #     return 가지치기
    
    
    #종료조건(n에 관련)-> 정답처리는 여기서
    if n == N:
        if cnt == CNT and sm == K:
            ans += 1
        return

    #하부호출
    dfs(n+1, cnt+1, sm+lst[n])    #사용하는 경우
    dfs(n+1, cnt, sm)             #사용하지 않는 경우


T = int(input())
for tc in range(1, T + 1):
    CNT, K = map(int, input().split())
    N = 12
    lst = [n for n in range(1, N+1)]
    ans = 0
    # main loop에서는 dfs의 가장 위 노드를 호출
    dfs(0, 0, 0)
    #종료조건 선택된 갯수 합
    #n, cnt, sm
    print(f'#{tc} {ans}')