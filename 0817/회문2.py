T = 10

for test_case in range(1, T + 1):
    test = int(input())
    # 표 저장
    arr = [input() for _ in range(100)]
    # 90도 뒤집어서 저장 (세로 회문 확인용)
    new_arr = list(map(list, zip(*arr)))
    # 1 = 가로 길이, 2 = 세로 길이
    length_1 = 0
    length_2 = 0
    max_length = 0

    # 모든 범위에 대해서 모든 칸을 검사
    for i in range(100):
        for j in range(100):
            for t in range(j+1, 101):
                tmp_1 = arr[i][j:t]
                tmp_2 = new_arr[i][j:t]
                # 회문 검사
                if tmp_1 == tmp_1[::-1]:
                    length_1 = len(tmp_1)
                # 회문 검사
                if tmp_2 == tmp_2[::-1]:
                    length_2 = len(tmp_2)
                # 길이 최대값 검사
                max_length = max(length_1, length_2, max_length)

    print(f'#{test} {max_length}')