import sys
# L = 선택한 팀원 수, n = 현재 조합 탐색의 인덱스
def team(L, n):
    global result
    # 팀원 수가 조건에서 요구하는 수와 같으면
    if L == N//2:
        # 스타트팀, 링크팀 점수 저장용
        a = 0
        b = 0
        for i in range(N):
            for j in range(N):
                # visited에 표시되어 있다면 = 스타트팀
                if visited[i] == 1 and visited[j] == 1:
                    a += s[i][j]
                # visited에 표시되지 않았다면 = 링크팀
                elif visited[i] == 0 and visited[j] == 0:
                    b += s[i][j]
        # 결과의 최솟값 저장
        result = min(result, abs(a-b))
        return
    # 백트래킹 이용해 조합 구함
    for i in range(n, N):
        # 현재 선수가 선택되지 않았다면
        if visited[i] == 0:
            # 현재 선수 선택 후
            visited[i] = 1
            # 다음 선수 찾으러 감
            team(L+1, i+1)
            # 돌아온 다음 해당 선수를 제외한 조합을 구하기 위해 상태 돌림
            visited[i] = 0


# N = 팀 개수
N = int(sys.stdin.readline())
# s = 능력치
s = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 방문 표시
visited = [0]*N
# 첫번째는 선택함 ==> 중복을 줄이기 위해 선택함
visited[0] = 1
# 최솟값 저장용
result = 99999
# 첫번째를 선택했기 때문에 시작점은 1부터
team(1, 1)
print(result)

