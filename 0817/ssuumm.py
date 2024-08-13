T = 10
for test_case in range(1, T+1):
    dummy = input()

    arr = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0
    # 가로
    for i in range(100):
        max_sum = max(sum(arr[i]), max_sum)
    # 세로
    for i in range(100):
        num = 0
        for j in range(100):
            num += arr[j][i]
        max_sum = max(num, max_sum)
    # 대각선
    left = 0
    right = 0
    for i in range(100):
        left += arr[i][i]
        right += arr[99-i][i]

    max_sum = max(left, right, max_sum)
    print(f'#{test_case} {max_sum}')