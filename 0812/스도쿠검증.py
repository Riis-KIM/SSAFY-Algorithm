T = int(input())

for test_case in range(1, T+1):

    arr =[list(map(int, input().split())) for _ in range(9)]

    flag = 1

    # 가로 검증
    for i in range(9):
        s1 = set()
        for j in range(9):
            s1.add(arr[i][j])
        if len(s1) != 9:
            flag = 0
            break

    # 세로 검증
    for i in range(9):
        s1 = set()
        for j in range(9):
            s1.add(arr[j][i])
        if len(s1) != 9:
            flag = 0
            break

    # 3*3 검증
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            s1 = set()

            for k in range(i, i+3):
                for t in range(j, j+3):
                    s1.add(arr[k][t])
            if len(s1) != 9:
                flag = 0
                break


    print(f'#{test_case} {flag}')