# 그리디 알고리즘, 7800ms 나옴
# N = int(input())

# arr = []
# for _ in range(N):
#     arr.append(int(input()))

# arr.sort()        # 오름차순 정렬로
# ans = 0           # 답 저장용
# while len(arr) != 1:      # 배열에 1개 남을때까지
#     a = arr.pop(0)        # 작은 애들 2개 꺼내서 더하고 저장
#     b = arr.pop(0)
#     tmp = a+b
#     ans+=tmp
#     arr.append(tmp)       # 배열에 넣고
#     arr.sort()            # 정렬해서 다시 오름차순으로 만듬

# print(ans)

# 우선순위 큐, 힙 사용해서 구현, 자동으로 오름차순으로 정렬됨, 230ms나옴
import heapq
N = int(input())

arr = []
for _ in range(N):
    heapq.heappush(arr, int(input()))

ans = 0
while len(arr) != 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    tmp = a+b
    ans+=tmp
    heapq.heappush(arr, tmp)

print(ans)