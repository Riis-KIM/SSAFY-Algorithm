T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    arr = list(map(int, input().split()))

    # 정렬
    arr.sort()

    ans = []

    # 큰 숫자 작은숫자 번갈아가며 넣음
    for i in range(N//2):
        ans.append(arr[-i-1])
        ans.append(arr[i])
    # 홀수일 경우 정가운데 1개가 남기때문에 추가함
    if N%2 == 1:
        ans.append(arr[N//2])

    # 10개까지만 출력
    print(f'#{test_case}', *ans[:10])