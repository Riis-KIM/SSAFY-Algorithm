T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 최대 최소 저장용
    min_num = arr[0]
    max_num = arr[0]

    for item in arr:
        if item < min_num:
            min_num = item
        if item > max_num:
            max_num = item

    print(f'#{test_case} {max_num-min_num}')