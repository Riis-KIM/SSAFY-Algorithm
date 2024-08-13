T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    arr = list(map(int, input().split()))

    max_sum = 0
    min_sum = 999999
    for i in range(N-M+1):
        sum = 0
        for j in range(M):
            sum += arr[i+j]

        if sum > max_sum:
            max_sum = sum
        if sum < min_sum:
            min_sum = sum

    print(f'#{test_case} {max_sum-min_sum}')