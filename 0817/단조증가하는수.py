T = int(input())

for test_case in range(1, T+1):
    # 전체 숫자 개수
    N = int(input())
    # 숫자 리스트
    arr = list(map(int, input().split()))

    # 단조가 없을 경우 -1을 출력하기 위함임
    max_num = -1

    # 전체 숫자에 대해서 단조계산
    for i in range(N):
        for j in range(i+1, N):
            # 단조 계산
            danjo = str(arr[i]*arr[j])
            flag = True
            for j in range(1, len(danjo)):
                # 앞뒤 숫자 크기 비교해서 단조 판별
                if int(danjo[j]) < int(danjo[j-1]):
                    flag = False
                    break
            # 단조일 경우 최대값 비교 후 갱신
            if flag:
                # max 함수 쓰니까 안되던데 왜 안된거지? 모르겠음
                if max_num < int(danjo):
                    max_num = (int(danjo))

    print(f'#{test_case} {max_num}')