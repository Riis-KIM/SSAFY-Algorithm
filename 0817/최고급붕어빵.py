def bunge(M, K, people):
    # 초, 빵 , 사람
    i = -1
    bread = 0
    j = 0
    while j < len(people):
        i += 1
        # 제작 시간에 맞춰 빵 제작, 0초일때는 방금 장사를 시작해서 빵을 준비할 수가 없음
        if i % M == 0 and i != 0:
            bread += K
        # 사람 도착
        if people[j] <= i:
            # 빵이 남아 있다면 주고 다음 손님 생각
            if bread > 0:
                bread -= 1
                j += 1
            else:
                return 'Impossible'
    return 'Possible'

T = int(input())

for test_case in range(1, T+1):
    # N = 사람 개수, M = 1회당 제작 시간, K = 1회당 제작 개수
    N, M, K = map(int, input().split())
    # 도착 시간 표시
    people = list(map(int, input().split()))
    # 빨리 도착하는 순으로 정렬
    people.sort()
    ans = bunge(M,K,people)
    print(f'#{test_case} {ans}')