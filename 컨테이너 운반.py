T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lstw = list(map(int, input().split()))
    lstt = list(map(int, input().split()))

    lstw.sort(reverse=True)
    lstt.sort(reverse=True)

    #하나씩 짐 내리면서 현재 트럭에 가능한지 체크
    i = 0
    ans = 0
    for n in lstw:
        if n <= lstt[i]:
            ans += n
            i += 1
            if i == M:
                break


    print(f'#{tc} {ans}')