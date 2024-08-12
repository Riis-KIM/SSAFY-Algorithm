T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    count = 0
    # 가로 검사
    for i in range(N):
        for j in range(N-M+1):
            # 전부 빈칸일때
            if 0 not in arr[i][j:j+M]:
                # 왼쪽 벽일때
                if j == 0:
                    if arr[i][j+M] == 0:
                        count+=1
                # 오른쪽 벽일때
                elif j+M == N:
                    if arr[i][j-1] == 0:
                        count+=1
                else:
                    if arr[i][j-1] == 0 and arr[i][j+M] == 0:
                        count+=1

    # 세로 검사
    for j in range(N):
        for i in range(N-M+1):
            # 전부 빈칸일때
            # if 0 not in arr[i:i+M-1][j]:
            if all(arr[k][j] == 1 for k in range(i, i + M)):
                # 위쪽 벽일때
                if i == 0:
                    if arr[i+M][j] == 0:
                        count+=1
                # 아래쪽 벽일때
                elif i+M == N:
                    if arr[i-1][j] == 0:
                        count+=1
                else:
                    if arr[i-1][j] == 0 and arr[i+M][j] == 0:
                        count+=1

    print(f'#{test_case} {count}')


