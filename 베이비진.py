def check():
    global ans
    tr = 0
    if (p[0] == p[1] == p[2]) or (p[0] + 1 == p[1] and p[1] + 1 == p[2]):
        tr += 1
    if (p[3] == p[4] == p[5]) or (p[3] + 1 == p[4] and p[4] + 1 == p[5]):
        tr += 1
    if tr == 2:
        ans = 'Baby Gin'


def f(i, k):
    if i == k:
        check()
    else:
        for j in range(k):
            if used[j] == 0:
                used[j] = 1
                p[i] = arr[j]
                f(i + 1, k)
                used[j] = 0


T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input()))
    p = [0] * 6
    used = [0] * 6
    ans = 'Lose'
    f(0, 6)
    print(f'#{tc} {ans}')