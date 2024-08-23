arr = [[0]*101 for _ in range(101)]

cnt = 0
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    # 범위 내에 빈칸이면 색칠하고 카운트 +1, 색칠되어 있으면 패스
    for i in range(y1, y2):
        for j in range(x1, x2):
            if arr[i][j] == 0:
                cnt += 1
                arr[i][j] = 1

print(cnt)