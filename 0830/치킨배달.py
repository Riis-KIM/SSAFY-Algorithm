def find_loc(k, num):
    global min_loc, M
    # 치킨집을 M개 골랐을 때 길이 계산
    if num == M:
        # 이번에 고른 치킨집들로 최솟값을 계산
        tmp1 = 0
        for i in home:
            # 해당 집에서 가장 가까운 치킨집 찾기
            tmp2 = 9999999
            for j in s:
                tmp2 = min(tmp2, abs(i[0] - j[0]) + abs(i[1] - j[1]))
            tmp1 += tmp2
        # 이번에 고른 치킨집들과 다른 치킨집들로 위치 계산해봤을때 최솟값
        min_loc = min(min_loc, tmp1)
        return

    # 스택에 치킨집 추가
    for c in range(k, total_chicken):
        s.append(chicken[c])
        find_loc(c + 1, num + 1)
        s.pop()


# 도시 길이, 치킨집 개수
N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]

# 도시 위치, 치킨집 위치 찾음
home = []
chicken = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])

# 스택 선언, 최솟값 저장용, 전체 치킨집 개수
s = []
min_loc = 9999999
total_chicken = len(chicken)
find_loc(0, 0)

print(min_loc)