T = 10

for test_case in range(1, T+1):
    dump = int(input())

    arr = list(map(int, input().split()))

    for _ in range(dump):
        high = 0
        low = 0
        for i in range(len(arr)):
            if arr[high] < arr[i]:
                high = i
            if arr[low] > arr[i]:
                low = i
        arr[high] -= 1
        arr[low] += 1

    for i in range(len(arr)):
        if arr[high] < arr[i]:
            high = i
        if arr[low] > arr[i]:
            low = i

    print(f'#{test_case} {arr[high] - arr[low]}')
