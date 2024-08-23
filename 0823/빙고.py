
def isbinggo(i, j, binggo):
    # 가로, 해당 행 다 더해서 5면 빙고
    tmp = 0
    for t in range(5):
        tmp += visited[i][t]
    if tmp == 5:
        binggo += 1
    # 세로, 해당 열 다 더해서 5면 빙고
    tmp = 0
    for t in range(5):
        tmp += visited[t][j]
    if tmp == 5:
        binggo += 1

    # 대각선 확인 // 대각선에 해당하는 칸일 경우만
    for check1, check2 in [[0,0], [1,1], [2,2], [3,3], [4,4]]:
        if check1 == i and check2 == j:
            tmp = 0
            for a in range(5):
                tmp += visited[a][a]
            if tmp == 5:
                binggo+=1
    # 대각선 확인 // 대각선에 해당하는 칸일 경우만
    for check1, check2 in [[4,0], [3,1], [2,2], [1,3], [0,4]]:
        if check1 == i and check2 == j:
            tmp = 0
            for a in range(5):
                tmp += visited[a][4-a]
            if tmp == 5:
                binggo+=1

    return binggo
# 받아온 숫자가 어디에 있는지 확인하고 방문 표시
def check(item):
    nowx = 0
    nowy = 0
    for i in range(5):
        for j in range(5):
            if item == arr[i][j]:
                visited[i][j] = 1
                nowx = j
                nowy = i
    return nowy, nowx

arr = [list(map(int, input().split())) for _ in range(5)]
visited = [[0]*5 for _ in range(5)]
# 6부터 10까지
cnt = 0
binggo = 0
for _ in range(5):
    # 숫자 받아옴
    bing = list(map(int, input().split()))
    # 숫자 어디있는지
    for item in bing:
        cnt += 1
        # 숫자 표시
        nowy, nowx = check(item)
        binggo = isbinggo(nowy, nowx, binggo)
        if binggo >= 3:
            print(cnt)
            break
    if binggo >= 3:
        break

