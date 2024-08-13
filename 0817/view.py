T = 10

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    count = 0
    for i in range(2, N-2):
        if arr[i] > arr[i-1] and arr[i] > arr[i-2] and arr[i] > arr[i+1] and arr[i] > arr[i+2]:
            count += arr[i] - max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])

    print(f'#{test_case} {count}')