T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    bits = int(input(), 16) 
    ans = cnt = 0
    for i in range(N*4):
        if bits & (1<<i):
            cnt += 1
            ans = max(ans, cnt)          
        else:
            cnt = 0
    print(f'#{tc} {ans}')             