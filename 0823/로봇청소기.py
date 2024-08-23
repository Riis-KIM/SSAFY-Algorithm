def clean(r, c, d, N, M):
    cnt = 0
    i, j = r, c
    delta = [[-1, 0], [0, -1], [1, 0], [0, 1]]  # 북, 서, 남, 동
    nowloc = (4-d)%4

    while True:
        # 현재 칸 청소 안되었다면 청소
        if arr[i][j] == 0 and visited[i][j] == 0:
            cnt += 1
            visited[i][j] = 1  # 현재 위치 방문 처리

        # 주변 칸 확인
        empty = False
        for di, dj in delta:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 0 and visited[ni][nj] == 0:
                    empty = True

        if empty:
            # 주변에 청소되지 않은 빈 칸이 있는 경우
            while True:
                # 반시계 방향으로 회전
                nowloc = (nowloc + 1) % 4
                ci, cj = i + delta[nowloc][0], j + delta[nowloc][1]

                # 회전 후 청소되지 않은 빈 칸이 있다면 한 칸 전진
                if 0 <= ci < N and 0 <= cj < M and arr[ci][cj] == 0 and visited[ci][cj] == 0:
                    i, j = ci, cj
                    break
        else:
            # 주변에 청소되지 않은 빈 칸이 없을 경우 후진
            ci, cj = i - delta[nowloc][0], j - delta[nowloc][1]
            if 0 <= ci < N and 0 <= cj < M and arr[ci][cj] == 0:
                i, j = ci, cj
            else:
                # 후진할 수 없는 경우 작동 중지
                return cnt


# col, row
N, M = map(int, input().split())

# col, row, direction
r, c, d = map(int, input().split())

# 청소구역
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

print(clean(r, c, d, N, M))
