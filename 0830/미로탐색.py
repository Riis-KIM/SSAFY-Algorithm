from collections import deque

def find_miro():
    global N, M, ans

    # BFS 큐 초기화
    q = deque([(0, 0, 1)])  # (현재 인덱스 i, 현재 인덱스 j, 현재 카운트)
    visited[0][0] = 1  # 시작점 방문 표시

    while q:
        i, j, cnt = q.popleft()

        # 목표 지점에 도착했을 때 최솟값 업데이트
        if i == N-1 and j == M-1:
            ans = min(ans, cnt)
            continue

        # 델타를 이용해 갈 수 있는 경로로 이동
        for t in range(4):
            ni, nj = i + dy[t], j + dx[t]
            if 0 <= ni < N and 0 <= nj < M and miro[ni][nj] == 1 and not visited[ni][nj]:
                visited[ni][nj] = 1
                q.append((ni, nj, cnt + 1))


N, M = map(int, input().split())

# 미로 저장용
miro = [list(map(int, input())) for _ in range(N)]

# 방문 표시
visited = [[0] * M for _ in range(N)]

# 답 저장용
ans = N * M

# 델타
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 정답 찾기
find_miro()

print(ans)
