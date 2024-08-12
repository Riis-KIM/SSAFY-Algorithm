T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_num = 0
    if N <= M:
        for i in range(M-N+1):
            num = 0
            for j in range(N):
                num += A[j] * B[i+j]

            if max_num < num:
                max_num = num
    else:
        for i in range(N - M + 1):
            num = 0
            for j in range(M):
                num += A[i+j] * B[j]

            if max_num < num:
                max_num = num

    print(f'#{test_case} {max_num}')