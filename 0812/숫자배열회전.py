T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{test_case}')
    for i in range(N):
        # 90도
        for j in range(N):
            print(arr[N-j-1][i], end='')
        print(' ', end='')
        # 180도
        for j in range(N):
            print(arr[N-i-1][N-j-1], end='')
        print(' ', end='')
        # 270도
        for j in range(N):
            print(arr[j][N-i-1], end='')
        print()