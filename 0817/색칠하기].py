T = int(input())

for test_case in range(1, T+1):

    arr = [[0 for _ in range(10)] for _ in range(10)]

    N = int(input())

    for i in range(N):
        r1, c1, r2, c2, c = map(int, input().split())

        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                arr[i][j] += c

    count = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                count+=1
    print(f'#{test_case} {count}')