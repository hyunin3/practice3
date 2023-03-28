def check():
    global ans
    
    runtri = 0
    if (p[0]==p[1]==p[2]) or (p[0]+1==p[1] and p[1]+1==p[2]):
        runtri +=1
    if (p[3]==p[4]==p[5]) or (p[3]+1==p[4] and p[4]+1==p[5]):
        runtri +=1    
    if runtri == 2:
        ans = 1


def f(i, k):  #p[i]값을 결정
    
    if i == k:
        check()
    else:
        for j in range(k):
            if u[j] == 0:  #A[j] 미사용이면     
                u[j] = 1   #A[j] 사용으로 표시
                p[i] = lst[j] #p[i] 결정
                f(i+1, k) #p[i+1] 결정하러 이동
                u[j] = 0    
        

T = int(input())
for tc in range(1, T+ 1):
    ans = 0
    lst = list(map(int, input()))
    p = [0] * 6
    u = [0] * 6
    f(0, 6)
    print(f'#{tc} {ans}')



