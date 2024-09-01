def bfs(i, j, cnt, total):
    global N, M, max_num

    # 4칸이면
    if cnt == 4:
        # 현재까지의 점수와 최댓값 비교
        max_num = max(max_num, total)
        return

    # 델타를 이용해 방문하지 않은 곳 중 갈 수 있는 곳 찾기
    for t in range(4):
        ni, nj = i + di[t], j + dj[t]
        if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0:
            # 다음칸 방문 표시
            visited[ni][nj] = 1
            # 다음칸으로 이동
            bfs(ni, nj, cnt + 1,total + arr[ni][nj])
            # 방문 표시 삭제
            visited[ni][nj] = 0


# T자 확인용
def Tmino(i, j):
    global N, M, max_num
    # 4방향 확인 후 저장
    tmp = []
    for t in range(4):
        ni, nj = i + di[t], j + dj[t]
        if 0 <= ni < N and 0 <= nj < M:
            tmp.append(arr[ni][nj])

    # 4칸 다 확인이 될 경우, 4가지 방향에 대해서 최댓값 확인
    if len(tmp) == 4:
        for k in range(4):
            ans = tmp[k] + tmp[(k+1)%4] + tmp[(k-1)%4] + arr[i][j]
            max_num = max(max_num, ans)
    # 3칸만 확인이 될 경우, 한가지 경우밖에 없기 때문에 전부 더함
    elif len(tmp) == 3:
        ans = arr[i][j] + sum(tmp)
        max_num = max(max_num, ans)
    # 그외는 T자가 만들어지지 않음
    return

# 가로길이, 세로길이
N, M = map(int, input().split())
# 배열저장
arr = [list(map(int, input().split())) for _ in range(N)]

# 최대값 저장용
max_num = 0
# BFS 사용
visited = [[0] * M for _ in range(N)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 모든 칸을 시작지점으로 지정
for i in range(N):
    for j in range(M):
        # 해당 칸을 시작점으로 사용 후
        visited[i][j] = 1
        bfs(i, j,1 , arr[i][j])
        # 초기화
        visited[i][j] = 0
        # T자 확인용
        Tmino(i,j)

print(max_num)