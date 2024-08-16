def find_garo(i, j):
    # 가로 확인
    garo = 1
    while True:
        if j+1 <= len(arr):
            if arr[i][j+1] != 0:
                j += 1
                garo += 1
            else:
                return garo
def find_sero(i, j):
    # 세로 확인
    sero = 1
    while True:
        if i+1 <= len(arr):
            if arr[i+1][j] != 0:
                i += 1
                sero += 1
            else:
                return sero


T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = []
    # 전체 돌다가 0이 아닌 숫자를 찾으면
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                # 가로, 세로 최대 길이 구함
                a = find_garo(i,j)
                b = find_sero(i,j)
                # 행렬의 크기, 가로, 세로 저장
                ans.append([a*b, b, a])
                # 해당 행렬에 해당하는 부분 숫자 0으로 변경
                for t in range(i, i+b):
                    for q in range(j, j+a):
                        arr[t][q] = 0
    # 행렬의 크기별로 정렬
    ans.sort()
    # 출력
    print(f'#{test_case}', len(ans), end = ' ')
    for a,b,c in ans:
        print(b, c, end = ' ')
    print()