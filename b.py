T = int(input())
for tc in range(1, T + 1):
    N, st = input().split()
    lst = []
    for ch in st:
        if ch.isdigit():
            n = ord(ch) - ord('0')
        else:
            n = ord(ch) - ord('A') + 10
        for pos in (3,2,1,0):
            lst.append((n>>pos) & 1)
    print(f'#{tc} {"".join(map(str, lst))}')                     