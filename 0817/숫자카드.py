T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    num = input()
    # 숫자 저장용 배열
    arr = [0]*10
    # 개수 저장
    for item in num:
        arr[int(item)] += 1

    max_idx = 9
    # 최대값 비교
    for i in range(9, -1, -1):
        if arr[max_idx] < arr[i]:
            max_idx = i

    print(f'#{test_case} {max_idx} {arr[max_idx]}')