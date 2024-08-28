def find_omok(i, j, cnt, direction, color):
    cnt += 1
    # 같은 방향으로 나아가는데
    ni, nj = i + di[direction], j + dj[direction]
    # 범위 내에 색깔도 같으면
    if 0<=ni<19 and 0<=nj<19 and arr[ni][nj] == color:
        if find_omok(ni, nj, cnt, direction, color):
            return True
    # 더이상 없을 때
    else:
        # 카운트가 5라면 => 오목이라면
        if cnt == 5:
            return True
        # 그외라면(육목포함)
        else:
            return False


def find_al():
    # 범위 내 바둑알 찾음
    for i in range(19):
        for j in range(19):
            if arr[i][j] != 0:
                # 색깔 지정
                al = arr[i][j]
                # 델타 이용해서 갈 수 있는 방향으로
                for t in range(4):
                    ni, nj = i + di[t], j + dj[t]
                    # 다음 바둑알을 찾았을때
                    if 0 <= ni < 19 and 0 <= nj < 19 and arr[ni][nj] == al:
                        # 만약 뒤로 바둑알이 있다면 = 이미 해당 방향을 고려했음 or 아직 시작점이 아님
                        if 0<=i-di[t]<19 and 0<=j-dj[t]<19 and arr[i-di[t]][j-dj[t]] == al:
                            break
                        # 오목을 찾았다면 색과 위치 반환
                        if find_omok(ni, nj, 1, t, al):
                            return [al, i+1, j+1]
    # 그러지 않을 경우 0 반환
    return [0]


arr = [list(map(int, input().split())) for _ in range(19)]

di = [-1, 0, 1, 1]
dj = [1, 1, 1, 0]

ans = find_al()
# 길이가 1이다 = 오목 못찾음
if len(ans) == 1:
    print(ans[0])
else:
    print(ans[0])
    print(ans[1], ans[2])


