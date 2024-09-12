from collections import deque

def bfs(s_i,s_j, e_i,e_j, N):       # 시작 좌표 i, j / 목표 좌표 i, j, 체스판 크기
    q = deque()
    q.append([s_i, s_j, 0])   # y, x, 현재 이동 횟수
    
    visited = [[float('inf')] * N for _ in range(N)]        # 이동 횟수 저장용
    visited[s_i][s_j] = 0           # 시작점 0으로

    while q:            # 큐에 남아있다면
        i, j, cnt = q.popleft()     # i, j, 현재 이동 횟수 꺼냄
        if i == e_i and j == e_j:       # 목표에 도달하면
            return cnt          # 이동 횟수 출력
        for t in range(8):          # 델타 사용
            ni, nj = i + di[t], j + dj[t]
            if 0<=ni<N and 0<=nj<N:         # 범위 내 일때
                if visited[ni][nj] > cnt+1:         # 다음에 이동하려는 칸이 이동 횟수보다 클 때 -> 현재까지 온 방법이 더 짧음
                    visited[ni][nj] = cnt+1         # 더 짧은 경로로 갱신
                    q.append([ni, nj, cnt+1])       # 다음 경로 찾으러감


T = int(input())

# 나이트 이동 경로 시계방향으로
di = [-2, -1, 1, 2, 2, 1, -1, -2]
dj = [1, 2, 2, 1, -1, -2, -2, -1]


for test_case in range(T):
    L = int(input())
    # y, x
    knight_y, knight_x = map(int, input().split())
    target_y, target_x = map(int, input().split())

    ans = bfs(knight_y,knight_x, target_y,target_x, L)

    print(ans)
