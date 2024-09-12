import heapq
'''
힙 라이브러리의 기본은 최소힙이기 때문에 그냥 사용하면 됨
'''
N = int(input())
q = []          # 힙 저장용
ans = []        # 답 저장용

for _ in range(N):
    tmp = int(input())
    if tmp == 0:            # 받은게 0일때
        if len(q):          # 배열에 값이 남아있다면
            ans.append(heapq.heappop(q))        # 정답에 답 저장
        else:
            ans.append(0)           # 없을 경우 0 저장
    else:
        heapq.heappush(q, tmp)      # 값일 경우 값 추가

for item in ans:        # 답 출력
    print(item)