T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    max_num = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            num = 0

            for t in range(M):
                for q in range(M):
                    num += arr[i+t][j+q]

            if max_num < num:
                max_num = num

    print(f'#{test_case} {max_num}')