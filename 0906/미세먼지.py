# 세로, 가로, 시간
R, C, T = map(int, input().split())
# 방 정보 받아옴
room = [list(map(int, input().split())) for _ in range(R)]
# 에어컨
air_purifiers = []
# 에어컨 위치 찾기
for i in range(R):
    for j in range(C):
        if room[i][j] == -1:
            air_purifiers.append((i, j))
# 델타
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 시간 초 만큼 반복
for _ in range(T):
    # 새 방에 먼지 이동한 모습 저장
    new_room = [[0] * C for _ in range(R)]
    # 새 방에 에어컨 위치 배치
    for a, b in air_purifiers:
        new_room[a][b] = -1

    # 먼지가 퍼졌을때의 방의 모습
    # 먼지 찾을 경우
    for i in range(R):
        for j in range(C):
            # 빈칸 or 에어컨 아닐때
            if room[i][j] >0:
                # 퍼지는 먼지 양
                spread = room[i][j]//5
                # 퍼지는 칸 수
                cnt = 0
                # 델타 사용
                for t in range(4):
                    ni, nj = i +di[t], j+dj[t]
                    # 범위 내에 에어컨 아닐 때
                    if 0 <= ni < R and 0 <= nj < C and room[ni][nj] != -1:
                                # 새로운 방에 퍼진 먼지 표시
                                new_room[ni][nj] += spread
                                # 퍼트린 방의 개수 저장
                                cnt += 1
                # 본인 자리의 먼지량 반영해서 추가
                new_room[i][j] += room[i][j] - (cnt * spread)

    # 에어컨 가동했을때의 방의 모습
    # 에어컨 가동할때 방의 모습 저장용
    new_room2 = [[0] * C for _ in range(R)]


    # 위쪽 에어컨
    up_i, up_j = air_purifiers[0]
    # 아래쪽 흐름 - 이전 칸의 먼지를 현재 칸에 저장하고 시작점은 0으로
    for j in range(2, C):
        new_room2[up_i][j] = new_room[up_i][j - 1]
    new_room2[up_i][1] = 0

    # 오른쪽 흐름 - 이전 칸의 먼지를 현재 칸에 저장함
    for i in range(0, up_i):
        new_room2[i][-1] = new_room[i + 1][-1]
        # 바람이 흐르지 않는 사이의 칸들에 대한 정보를 반영하기 위함
        if i != 0:
            for j in range(1, C - 1):
                new_room2[i][j] = new_room[i][j]

    # 위쪽 흐름 - 이전 칸의 먼지를 현재 칸에 저장
    for j in range(0, C - 1):
        new_room2[0][j] = new_room[0][j + 1]

    # 왼쪽 흐름 - 이전 칸의 먼지를 현재 칸에 저장
    for i in range(1, up_i):
        new_room2[i][0] = new_room[i - 1][0]


    # 아래쪽 에어컨
    down_i, down_j = air_purifiers[1]

    # 위쪽 흐름 - 이전 칸의 먼지를 현재 칸에 저장하고 시작점은 0으로
    for j in range(2, C):
        new_room2[down_i][j] = new_room[down_i][j - 1]
    new_room2[down_i][1] = 0

    # 오른쪽 흐름 - 이전 칸의 먼지를 현재 칸에 저장
    for i in range(down_i + 1, R):
        new_room2[i][-1] = new_room[i - 1][-1]

    # 아래쪽 흐름 - 아래쪽 벽을 기준으로 먼지 이동
    for j in range(C - 1):
        new_room2[-1][j] = new_room[-1][j + 1]

    # 왼쪽 흐름 - 이전 칸의 먼지를 현재 칸에 저장
    for i in range(down_i + 1, R - 1):
        new_room2[i][0] = new_room[i + 1][0]
        # 바람이 흐르지 않는 사이의 칸들에 대한 정보를 반영하기 위함
        for j in range(1, C - 1):
            new_room2[i][j] = new_room[i][j]

    # 미세먼지가 퍼지고 에어컨이 작동된 이후의 방의 모습을 저장
    room = new_room2


# 모든 방의 먼지 양 계산
ans = 0
for i in range(R):
    for j in range(C):
       if room[i][j] != -1:
           ans += room[i][j]
print(ans)
